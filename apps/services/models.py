from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from apps.main.models import BaseModel
from django.utils.text import slugify
from django.utils import timezone
from django.db.models.signals import pre_save


class Tag(BaseModel):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class ServicesPost(BaseModel):
    name = models.CharField(max_length=123)
    image = models.ImageField(upload_to='media/', )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blog_category')
    tags = models.ManyToManyField(Tag, related_name='blog_tag', null=True, blank=True)
    slug = models.SlugField(unique=True,)

    def __str__(self):
        return self.name


class Content(BaseModel):
    blog = models.ForeignKey(ServicesPost, on_delete=models.CASCADE, related_name='content', )
    content = RichTextField()
    quote = models.BooleanField(default=False)


class Comments(BaseModel):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='author')
    top_level_comment_id = models.IntegerField(null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,)
    blog = models.ForeignKey(ServicesPost, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    name = models.CharField(max_length=123)
    message = models.TextField()

    def __str__(self):
        return self .message
    @property
    def children(self):
        if not self.top_level_comment_id:
            return Comments.objects.filter(top_level_comment_id=self.id)
        return None


class ServiceLike(models.Model):
    blog = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)


def blog_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name + " - " + timezone.now().date().strftime('%Y-%m-%d %H:%M:%S.%f'))


pre_save.connect(blog_pre_save, sender=ServicesPost)


def comment_pre_save(sender, instance, *args, **kwargs):

    if instance.parent:
        if instance.parent.top_level_comment_id:
            instance.top_level_comment_id = instance.parent.top_level_comment_id
        else:
            instance.top_level_comment_id = instance.parent.id


pre_save.connect(comment_pre_save, sender=Comments)