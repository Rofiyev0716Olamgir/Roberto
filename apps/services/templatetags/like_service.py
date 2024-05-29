from django import template

from apps.services.models import ServiceLike

register = template.Library()


@register.filter(name='user_likes_blog')
def user_likes_blog(eid, user_id):
    return ServiceLike.objects.filter(blog_id=eid, author_id=user_id).exists()