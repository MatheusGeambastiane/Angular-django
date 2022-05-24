import django
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    costumer_status = models.BooleanField(default=False, verbose_name="Paciente", help_text="Cliente padrão, poderá marcar consultas")
    manager_status = models.BooleanField(default=False, verbose_name="Gestor médico", help_text="Poderá criar agendas médicas")

    
    
    def __str__(self) -> str:
        return self.username

