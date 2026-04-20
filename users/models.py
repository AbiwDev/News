from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    pass
    
    def __str__(self):
        return self.username
        