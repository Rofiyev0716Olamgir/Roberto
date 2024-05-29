from django import template

from apps.blog.models import BlogLike

register = template.Library()


@register.filter(name='user_likes_blog')
def user_likes_blog(eid, user_id):
    return BlogLike.objects.filter(blog_id=eid, author_id=user_id).exists()