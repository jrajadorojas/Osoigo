# Django
from django import template

register = template.Library()

@register.filter
def index(contact,i):
    return contact[i]