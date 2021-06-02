from django import template

register = template.Library()


@register.filter(name='weather')
def weather(text):
    """
    Returns a human readable version of the text

    """
    return ' '.join(text.split('_')).capitalize()
