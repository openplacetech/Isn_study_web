from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from web_app.models import PrivacyPolicy,Insights,Subscriber
from web_app.constrants import STATUS_TYPE
from web_app.email import send_newsletter_to_all_subscribers,send_html_email
from django.conf import settings
@receiver(pre_save, sender=PrivacyPolicy)
def ensure_single_true_status(sender, instance, **kwargs):
    if instance.status == "PUBLISHED":
        sender.objects.exclude(pk=instance.pk).update(status="UNPUBLISHED")

@receiver(post_save,sender = Insights)
def insights_email(sender,instance,created, **kwargs):
    request = kwargs.get('request', None)
    sub = Subscriber.objects.all()

    domain =settings.SITE_DOMAIN
    url = f"{domain}/insight/{instance.slug}"
    newsletter = {
        'title': instance.title,
        'image': f"{domain}{instance.cover_image.url}",
        'description': instance.summary,
        'link': url
    }
    email_list=[]
    for s in sub:
        email_list.append(s.email)
    send_newsletter_to_all_subscribers(email_list,url,newsletter)
    # send_html_email()

