from django.conf import settings
from django.db import models


class UserContacts(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=25)
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    birthday= models.DateField(label='Birthday')


    def __str__(self):
        return self.full_name
