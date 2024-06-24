# from django.db import models
# from ckeditor.fields import RichTextField
# from tinymce.models import HTMLField
# from base.models import BaseModel
# from django.utils.text import slugify
#
#
# # Create your models here.
# class ContactUs(BaseModel):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     subject = models.CharField(max_length=200)
#     message = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = 'contact_us'
#         verbose_name_plural = "Contact Us"


#
# class Subscriber(BaseModel):
#     name = models.CharField(max_length=100,null=True,default="")
#     email = models.EmailField()
#     def __str__(self):
#         return self.email
#     class Meta:
#         db_table = 'Subscriber'
#         verbose_name_plural = "Subscribers"

#
# class Insights(BaseModel):
#     title = models.CharField(max_length=100)
#     summary = models.TextField()
#     slug = models.SlugField(unique=True, blank=True)
#     content = HTMLField()
#     cover_image = models.ImageField(upload_to='blog_cover/',help_text="Upload a profile picture. The image will be stored in the 'blog_cover/' directory.")
#     keywords = models.TextField(help_text="Do not add more then five keyword this is only for SEO")
#     categories =
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             # Generate a unique slug based on the title
#             self.slug = slugify(self.title)
#             # Ensure the slug is unique
#             original_slug = self.slug
#             queryset = Insights.objects.filter(slug=original_slug)
#             counter = 1
#             while queryset.exists():
#                 self.slug = f'{original_slug}-{counter}'
#                 queryset = Insights.objects.filter(slug=self.slug)
#                 counter += 1
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.title
#     class Meta:
#         db_table = 'Insights'
#         verbose_name_plural = "ISN Insights"

# class InsightComments(BaseModel):
#     title = models.CharField(max_length=100)
#     email = models.EmailField()
#     subject = models.CharField()
#     blog = models.ForeignKey(related_name=Blog)
#     message = models.TextField()

class CurrierOpportunities(BaseModel):
    job_title = models.TextField()
    job_description = HTMLField()
    keyword = models.TextField(help_text="only for SEO write a keyword seperated by comma(,) eg: python,django,hr")

    class Meta:
        db_table = 'CurrierOpportunities'
        verbose_name_plural = "Currier Opportunities"


class ApplyForCurrier(BaseModel):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=40)
    cover_latter = models.TextField(blank=True)
    resume = models.FileField(upload_to="/resume")

    class Meta:
        db_table = 'isn_job_application'
        verbose_name_plural = "Job Applications"
