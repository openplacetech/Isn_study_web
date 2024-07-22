from django import template
from ISNstudy_web.settings import CALENDARY_URL
register = template.Library()

@register.filter(name='word_length')
def word_length(value):
    """Returns the length of the given word/string."""
    return len(value)

@register.filter(name='calendry_url')
def calendry_url():
    return CALENDARY_URL