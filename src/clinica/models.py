
from turtle import st
from account.models import CustomUser
from django.db import models
from datetime import datetime, date



# Create your models here.
class Specialty(models.Model):

    specialty_name = models.CharField(max_length=100, verbose_name="Nome da Especialidade")
    description = models.TextField(verbose_name="Descrição")

    class Meta:
        managed = True
        verbose_name= "Especiaidade"
        verbose_name_plural= 'Especialidades'

    def __str__(self) -> str:
        return self.specialty_name

class Medical(models.Model):

    name = models.CharField(max_length=100, verbose_name="Nome do médico", )
    crm = models.CharField(max_length=10, verbose_name="CRM do médico", help_text="Número do registro médico", 
                        blank=False, null=False, unique=True )
    email = models.EmailField(max_length=50, verbose_name="Email")
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True, verbose_name="Especialidade")
    is_active = models.BooleanField(default=True, verbose_name="Está ativo")

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = True
        verbose_name= "Médico"
        verbose_name_plural= 'Médicos'

class Hour(models.Model):

    CHOICES = (
		('08h-09h', '08h-09h'),
		('09h-10h', '09h-10h'),
		('10h-11h', '10h-11h'),
        ('11h-12h', '13h-14h'),
        ('14h-15h', '15h-16h'),
        ('16h-17h', '17h-18h'),
	)

    hours = models.CharField(max_length= 10,verbose_name="Horário", choices=CHOICES)

    def __str__(self) -> str:
        return self.hours
    
    class Meta:
        managed = True
        verbose_name= "Horário"
        verbose_name_plural= 'Horários'

class Schedule(models.Model):
    
    CHOICES = (
		('08h-09h', '08h-09h'),
		('09h-10h', '09h-10h'),
		('10h-11h', '10h-11h'),
        ('11h-12h', '13h-14h'),
        ('14h-15h', '15h-16h'),
        ('16h-17h', '17h-18h'),
	)

    medical_name = models.ForeignKey(Medical, verbose_name="Médico", on_delete=models.SET_NULL, null=True)
    day = models.DateField(verbose_name="dia", default=datetime.today)
    schedule = models.ForeignKey(Hour, verbose_name="Horário", on_delete=models.CASCADE)

    def _get_today(self):
        return datetime.today
    
    def __str__(self) -> str:
        
        return str(f"{self.medical_name} - {self.day.strftime('%d/%m/%Y')} - {self.schedule}")

    class Meta:
        managed = True
        verbose_name= 'Agenda'
        verbose_name_plural= 'Agendas'

class Exam(models.Model):


    Status_Choice = (
		('Agendada', 'Agendada'),
		('Cancelada', 'Cancelada'),
		('Espera', 'Espera'),
		('Realizada', 'Realizada'),
	)


    patient = models.ForeignKey(CustomUser, verbose_name="Paciente", on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, verbose_name="Especialidade da consulta", on_delete=models.CASCADE)
    medical = models.ForeignKey(Medical, verbose_name="Médico", on_delete=models.CASCADE)
    day = models.DateField(verbose_name="Data da Consulta")
    hour = models.ForeignKey(Hour,verbose_name="Horário", on_delete=models.CASCADE)
    calendly = models.OneToOneField(Schedule, verbose_name="Agenda médica", on_delete=models.CASCADE, null=True, unique=True)
    status = models.CharField(max_length=20 ,verbose_name="Status da Consulta", choices=Status_Choice)
    disponible = models.BooleanField(verbose_name="Consulta Disponível", default=True)
    
    # def expirated(self):
    #     date = datetime.today()
    #     day = self.day
    #     hour = self.hour

    #     scheduled = se

    #     if self.day and self.hour < date 


    def __str__(self) -> str:
        return str(f'{self.patient.username} - {self.calendly.day}  {self.calendly.schedule}')

    class Meta:
        managed = True
        verbose_name= "Consulta"
        verbose_name_plural= 'Consultas'