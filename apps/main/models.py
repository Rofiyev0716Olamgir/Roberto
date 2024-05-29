from django.db import models


class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contact(BaseModel):
    name = models.CharField(max_length=123)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Partner(BaseModel):
    name = models.CharField(max_length=123, null=True, blank=True)
    image = models.ImageField(upload_to='partner/')

    def __str__(self):
        return self.name


class Services(BaseModel):
    name = models.CharField(max_length=123, null=True, blank=True)
    image = models.ImageField(upload_to='services/', null=True)

    def __str__(self):
        return self.name