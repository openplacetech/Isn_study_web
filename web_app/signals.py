from django.db.models.signals import pre_save
from django.dispatch import receiver
from web_app.models import PrivacyPolicy
from web_app.constrants import STATUS_TYPE

@receiver(pre_save, sender=PrivacyPolicy)
def ensure_single_true_status(sender, instance, **kwargs):
    if instance.status == "PUBLISHED":
        sender.objects.exclude(pk=instance.pk).update(status="PUBLISHED")