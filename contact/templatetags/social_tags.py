from django import template
from contact.models import Social, About


register = template.Library()


@register.simple_tag()
def get_social_links():
    """return links social networks"""
    return Social.objects.all()


@register.simple_tag()
def get_about():
    """return about"""
    return About.objects.last()


