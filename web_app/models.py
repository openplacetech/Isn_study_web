from django.db import models
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField
from base.models import BaseModel
from django.utils.text import slugify
from web_app.constrants import COUNTRY_CHOICES,REGION_TYPE,SOCIALMEDIA_TYPE,JOB_CATEGORY,JOB_TYPE,JOB_MODE,INSIGHTS_CATEGORY,INTERESTED_SERVICE,CONTACT_PHONE_TYPE,GENDER_TYPE,STATUS_TYPE,PAY_PERIOD_TYPE
from django.contrib.auth.models import User

class PartnershipRequest(BaseModel):
    institute_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    email = models.EmailField()
    phone_no = models.CharField(max_length=200)
    interested_service = models.CharField(max_length=100)
    message = models.TextField()
    is_accept_privacy_policy = models.BooleanField(default=False)
    def __str__(self):
        return self.institute_name

    class Meta:
        db_table = 'partnership_request'
        verbose_name_plural = "Partnership Request"


class Subscriber(BaseModel):
    name = models.CharField(max_length=100,null=True,default="",blank=True)
    email = models.EmailField()
    def __str__(self):
        return self.email

    class Meta:
        db_table = 'Subscriber'
        verbose_name_plural = "Subscribers"


class PrivacyPolicy(BaseModel):
    name = models.CharField(max_length=200,default="Privacy and Policy")
    content = HTMLField()
    status = models.CharField(choices=STATUS_TYPE,max_length=200,blank=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'privacy_policy'
        verbose_name_plural = "privacy policy"


class StudyDestinationOfNepali(BaseModel):
    region = models.CharField(max_length=100,choices=REGION_TYPE)
    country = models.CharField(max_length=100)
    student_no = models.CharField(max_length=100)
    class Meta:
        db_table = 'NumberOfStudentStudy'
        verbose_name_plural = "Student Number"

    def __str__(self):
        return self.country

    def save(self, *args, **kwargs):
        if self.country:
            self.name = self.country.capitalize()
        super().save(*args, **kwargs)



class Insights(BaseModel):
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    summary = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    content = HTMLField()
    cover_image = models.ImageField(upload_to='blog_cover/',help_text="Upload a cover picture. which height recommended size is 2,00x1,334 ")
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

    def insight_name(self):
        return self.insight.title

class CareerOpportunities(BaseModel):
    job_title = models.TextField()
    job_summary = models.TextField(max_length=500,default="" ,help_text="Job summary should less then 500 character")
    job_description = HTMLField()
    category = models.CharField(choices=JOB_CATEGORY,max_length=100)
    keyword = models.TextField(help_text="only for SEO write a keyword seperated by comma(,) eg: python,django,hr")
    job_mode = models.CharField(choices=JOB_MODE,max_length=50)
    job_type = models.CharField(choices=JOB_TYPE,max_length=50)
    job_status = models.CharField(choices=STATUS_TYPE,max_length=50)
    slug = models.SlugField(unique=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.job_title)
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
        db_table = 'CareerOpportunities'
        verbose_name_plural = "Career Opportunities"


class ISNTeam(BaseModel):
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=300)
    profile_image = models.ImageField(upload_to="team_profile" , help_text="recommended size is 612x408")
    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "teams"
        verbose_name_plural = "Our Teams"


class SocialMedia(BaseModel):
    name = models.CharField(max_length=100,choices=SOCIALMEDIA_TYPE,unique=True)
    followers = models.CharField(max_length=100,default="",blank=True)
    link = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "social_media"
        verbose_name_plural = "Social Media"


class Testimonials(BaseModel):
    photo = models.ImageField(upload_to="testimonial/photo",null=True,blank=True,help_text="Recommended size is 500x500")
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "testimonial"
        verbose_name_plural = "Testimonials"

class ApplyForCareer(BaseModel):
    job = models.ForeignKey(CareerOpportunities,on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=40)
    contact_phone_type = models.CharField(max_length=200,choices=CONTACT_PHONE_TYPE,blank=True,null=True)
    country = models.CharField(max_length=100,choices=COUNTRY_CHOICES,blank=True,null=True)
    profile_link = models.URLField(blank=True,null=True)
    profile_link_type = models.CharField(max_length=100,blank=True,null=True)
    expected_salary = models.CharField(max_length=200,blank=True,null=True)
    currency_type = models.CharField(max_length=200, default="USD")
    pay_period = models.CharField(max_length=100,choices=PAY_PERIOD_TYPE,blank=True,null=True)
    resume = models.FileField(upload_to="resume")
    availability_or_notice_period= models.CharField(max_length=300,blank=True,null=True)
    gender = models.CharField(max_length=100,choices=GENDER_TYPE,blank=True,null=True)
    veteran_status = models.CharField(max_length=100,blank=True,null=True)
    race_ethnicity = models.CharField(max_length=100,blank=True,null=True)
    disability = models.CharField(max_length=100,blank=True,null=True)
    legal_name = models.CharField(max_length=100,blank=True,null=True)
    other_job_consider = models.BooleanField(default=False,help_text="I authorize ISN to consider me for other job opportunities for the next 36 months within ISN in addition to the specific job I am applying for.")
    required_immigration_sponsorship = models.BooleanField(default=False,help_text='Will you now or in the future require immigration sponsorship for employment with ISN?',blank=True,null=True)
    is_previously_employed= models.BooleanField(default=False,help_text='Have you previously been employed by ISN?',blank=True,null=True)
    is_former_current_intern_or_contractor = models.BooleanField(default=False,help_text='Are you a former/current intern or contractor?',blank=True,null=True)
    receive_text_message = models.BooleanField(default=False,help_text='Do you consent to receiving text messages throughout your application process including but not limited to interview details, pre-employment screening notifications and reminders?',blank=True,null=True)
    def full_name(self):
        return self.first_name+ ' ' + self.last_name
    class Meta:
        db_table = 'isn_job_application'
        verbose_name_plural = "Job Applications"


class DataSource(BaseModel):
    source = HTMLField()
    status = models.CharField(choices=STATUS_TYPE, max_length=200, blank=True)
    def __str__(self):
        return self.source

    class Meta:
        db_table = 'DataSource'
        verbose_name_plural = "DataSource"