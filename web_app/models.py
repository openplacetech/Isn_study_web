from django.db import models
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField
from base.models import BaseModel
from django.utils.text import slugify
from web_app.constrants import COUNTRY_CHOICES,JOB_CATEGORY,JOB_TYPE,JOB_MODE,INSIGHTS_CATEGORY,INTERESTED_SERVICE,CONTACT_PHONE_TYPE,GENDER_TYPE,STATUS_TYPE
from django.contrib.auth.models import User

class PartnershipRequest(BaseModel):
    institute_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    email = models.EmailField()
    phone_no = models.CharField(max_length=200)
    interested_service = models.CharField(choices=INTERESTED_SERVICE,max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.institute_name

    class Meta:
        db_table = 'partnership_request'
        verbose_name_plural = "Partnership Request"


class Subscriber(BaseModel):
    name = models.CharField(max_length=100,null=True,default="")
    email = models.EmailField()
    def __str__(self):
        return self.email

    class Meta:
        db_table = 'Subscriber'
        verbose_name_plural = "Subscribers"


class PrivacyPolicy(BaseModel):
    content = HTMLField()
    status = models.CharField(choices=STATUS_TYPE,max_length=200,blank=True)
    class Meta:
        db_table = 'privacy_policy'
        verbose_name_plural = "privacy policy"


# class NumberOfStudentStudyInUS(BaseModel):
#     country = models.CharField(choices=COUNTRY_CHOICES,max_length=100)
#     student_no = models.IntegerField()
#
#     class Meta:
#         db_table = 'NumberOfStudentStudyInUS'
#         verbose_name_plural = "US Student Number"



class Insights(BaseModel):
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    summary = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    content = HTMLField()
    cover_image = models.ImageField(upload_to='blog_cover/',help_text="Upload a profile picture. The image will be stored in the 'blog_cover/' directory.")
    keywords = models.TextField(help_text="Do not add more then five keyword this is only for SEO")
    category = models.CharField(choices=INSIGHTS_CATEGORY,max_length=100)


    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate a unique slug based on the title
            self.slug = slugify(self.title)
            # Ensure the slug is unique
            original_slug = self.slug
            queryset = Insights.objects.filter(slug=original_slug)
            counter = 1
            while queryset.exists():
                self.slug = f'{original_slug}-{counter}'
                queryset = Insights.objects.filter(slug=self.slug)
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'Insights'
        verbose_name_plural = "ISN Insights"

class InsightComments(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    insight = models.ForeignKey(Insights,on_delete=models.CASCADE)
    message = models.TextField()
    class Meta:
        db_table = 'InsightComments'
        verbose_name_plural = "Insight Comments"

class CurrierOpportunities(BaseModel):
    job_title = models.TextField()
    job_description = HTMLField()
    category = models.CharField(choices=JOB_CATEGORY,max_length=100)
    keyword = models.TextField(help_text="only for SEO write a keyword seperated by comma(,) eg: python,django,hr")
    job_mode = models.CharField(choices=JOB_MODE,max_length=50)
    job_type = models.CharField(choices=JOB_TYPE,max_length=50)
    job_status = models.CharField(choices=STATUS_TYPE,max_length=50)
    slug = models.SlugField(unique=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate a unique slug based on the title
            self.slug = slugify(self.job_title)
            # Ensure the slug is unique
            original_slug = self.slug
            queryset = Insights.objects.filter(slug=original_slug)
            counter = 1
            while queryset.exists():
                self.slug = f'{original_slug}-{counter}'
                queryset = Insights.objects.filter(slug=self.slug)
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.job_title
    class Meta:
        db_table = 'CurrierOpportunities'
        verbose_name_plural = "Currier Opportunities"





class ApplyForCurrier(BaseModel):
    job = models.ForeignKey(CurrierOpportunities,on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=40)
    contact_phone_type = models.CharField(max_length=200,choices=CONTACT_PHONE_TYPE)
    country = models.CharField(max_length=100,choices=COUNTRY_CHOICES)
    profile_link = models.URLField()
    profile_link_type = models.CharField(max_length=100)
    expected_salary = models.CharField(max_length=200)
    resume = models.FileField(upload_to="resume")
    gender = models.CharField(max_length=100,choices=GENDER_TYPE)
    veteran_status = models.CharField(max_length=100)
    race_ethnicity = models.CharField(max_length=100)
    disability = models.CharField(max_length=100)
    legal_name = models.CharField(max_length=100)
    required_immigration_sponsorship = models.BooleanField(default=False,help_text='Will you now or in the future require immigration sponsorship for employment with ISN?')
    is_previously_employed= models.BooleanField(default=False,help_text='Have you previously been employed by ISN?')
    is_former_current_intern_or_contractor = models.BooleanField(default=False,help_text='Are you a former/current intern or contractor?')
    receive_text_message = models.BooleanField(default=False,help_text='Do you consent to receiving text messages throughout your application process including but not limited to interview details, pre-employment screening notifications and reminders?')
    class Meta:
        db_table = 'isn_job_application'
        verbose_name_plural = "Job Applications"