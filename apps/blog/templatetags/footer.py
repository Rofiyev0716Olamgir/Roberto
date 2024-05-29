from django import template
from apps.blog.models import BlogPost


register = template.Library()


@register.simple_tag
def footer1():
    return BlogPost.objects.order_by('-id')[:2]