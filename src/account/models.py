import django
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    teste = models.BooleanField(default=False)
    pass

