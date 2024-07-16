from django import template
register = template.Library()
from web_app.models import SocialMedia


@register.filter(name='word_length')
def word_length(value):
    """Returns the length of the given word/string."""
    return round(len(value)/1500)

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