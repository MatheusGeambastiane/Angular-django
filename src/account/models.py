import django
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    costumer_status = models.BooleanField(default=False, verbose_name="Paciente")
    manager_status = models.BooleanField(default=False, verbose_name="Gestor médico")

    
    
    def __str__(self) -> str:
        return self.username

