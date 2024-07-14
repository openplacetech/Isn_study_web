from django import template

register = template.Library()

@register.filter(name='word_length')
def word_length(value):
    """Returns the length of the given word/string."""
    return len(value)
