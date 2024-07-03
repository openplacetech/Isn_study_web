from django import template
register = template.Library()
from web_app.models import SocialMedia


@register.simple_tag
def facebook_followers():
    try:
        data = SocialMedia.objects.get(name="FACEBOOK")
        return data.link
    except SocialMedia.DoesNotExist:
        return None

@register.simple_tag
def instagram_followers():
    try:
        data = SocialMedia.objects.get(name="INSTAGRAM")
        return data.link
    except SocialMedia.DoesNotExist:
        return None