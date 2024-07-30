from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from web_app.models import PrivacyPolicy,Insights,Subscriber
from web_app.constrants import STATUS_TYPE
from web_app.email import send_newsletter_to_all_subscribers

@receiver(pre_save, sender=PrivacyPolicy)
def ensure_single_true_status(sender, instance, **kwargs):
    if instance.status == "PUBLISHED":
        sender.objects.exclude(pk=instance.pk).update(status="UNPUBLISHED")

# @receiver(post_save,sender = Insights)
# def insights_email(sender,instance,created, **kwargs):
#     sub = Subscriber.object.all()
#     url = "www.isn.com/insight/"+instance.slug
#     send_newsletter_to_all_subscribers(sub,url)

