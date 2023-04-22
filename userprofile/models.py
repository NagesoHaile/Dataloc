from django.db import models
from core.models import User
from django.conf import settings

class UserProfile(models.Model):
    profile_picture = models.ImageField(null=True)
    birth_date = models.DateField()
    country = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name}  {self.user.last_name}'
    
    
