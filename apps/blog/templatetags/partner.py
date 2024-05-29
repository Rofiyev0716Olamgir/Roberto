from django import template
from apps.main.models import Partner


register = template.Library()


@register.simple_tag()
def partner():
    return Partner.objects.all()