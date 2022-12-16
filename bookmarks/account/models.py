from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateTimeField(blank=True,null=True)
    photo = models.ImageField(upload_to='user/%Y/%m%d/',
                              blank=True)
    phone_number = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
