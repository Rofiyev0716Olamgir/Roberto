from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from apps.main.models import BaseModel
from django.utils.text import slugify
from django.utils import timezone
from django.db.models.signals import pre_save


class Room(BaseModel):
    name = models.CharField(max_length=123)
    price = models.IntegerField(default=100)
    max_person = models.IntegerField(default=1)
    size_a = models.IntegerField()
    size_b = models.IntegerField()
    bed = models.CharField(max_length=123, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    room_number1 = models.IntegerField()

    def __str__(self):
        return self.name


class Image(BaseModel):
    image = models.ImageField(upload_to='rooms/',)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_image')


class RoomContent(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='content_room')
    content = RichTextField()
    chek = models.BooleanField(default=False)


class RoomService(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='services_room')
    name = models.CharField(max_length=123)
    image = models.ImageField(upload_to='rooms/service/')


class Booking(BaseModel):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True, related_name='rooms_booking')
    check_in = models.DateField(null=True, blank=True)
    check_out = models.DateField(null=True, blank=True)
    adults = models.IntegerField(null=True, blank=True)
    children = models.IntegerField(null=True, blank=True)
    price_min = models.IntegerField(default=0, null=True, blank=True)
    price_max = models.IntegerField(default=3000, null=True, blank=True)

    def __str__(self):
        return self.room.name

    # @property
    # def amount(self):
    #     pass


def blog_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name + " - " + timezone.now().strftime('%Y-%m-%d %H:%M:%S.%f'))


pre_save.connect(blog_pre_save, sender=Room)




