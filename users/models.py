from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    username = None
    name = models.CharField(max_length=38)
    email = models.EmailField(max_length=200, unique=True)

    USERNAME_FIELD = 'email'
    auth_token = models.CharField(max_length=10)
    REQUIRED_FIELDS = []