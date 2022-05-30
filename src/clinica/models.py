from tabnanny import verbose
from django.db import models
from django.core.validators import EmailValidator, RegexValidator


from datetime import datetime, date

from django.forms import NullBooleanField, ValidationError

from account.models import CustomUser


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
    telefone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,14}$', message="O valor máximo é de 14 dígitos")

    medical_name = models.CharField(max_length=100, verbose_name="Nome do médico", )
    crm = models.CharField(max_length=10, verbose_name="CRM do médico", help_text="Número do registro médico", 
                        blank=False, null=False, unique=True )
    medical_email = models.EmailField( validators=[EmailValidator],max_length=50, verbose_name="Email")
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True, verbose_name="Especialidade")
    phone = models.CharField(validators=[telefone_validator], max_length=17, blank=True, null=True, verbose_name="Telefone")
    is_active = models.BooleanField(default=True, verbose_name="Está ativo")

    def __str__(self) -> str:
        return (f'{self.medical_name} - {self.specialty}')

    

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
    
    def day_validator(value):
        if date.today() > value:
            raise ValidationError (r'Não é possível cadastrar uma nova agenda para datas já passadas')  
        else:
            return value
   

    medical_name = models.ForeignKey(Medical, verbose_name="Médico", on_delete=models.PROTECT, null=True)
    day = models.DateField(validators=[day_validator],verbose_name="dia", default=datetime.today)
    hour = models.ForeignKey(Hour, null=True, verbose_name="horário", on_delete=models.PROTECT)
    def _get_today(self):
        return datetime.today
    
    def get_hour(self):
        return self.hour.hours


    def get_medical_name(self):
        
        return self.medical_name.medical_name

    def __str__(self) -> str:
        
        return (f"{self.medical_name} - {self.day.strftime('%d/%m/%Y')}")

    class Meta:
        managed = True
        unique_together = ('medical_name', 'day', 'hour')
        verbose_name= 'Agenda'
        verbose_name_plural= 'Agendas'

class Exam(models.Model):
    
    
    CHOICES = (
		('08h-09h', '08h-09h'),
		('09h-10h', '09h-10h'),
		('10h-11h', '10h-11h'),
        ('11h-12h', '13h-14h'),
        ('14h-15h', '15h-16h'),
        ('16h-17h', '17h-18h'),
	)

    # Status_Choice = (
	# 	('Agendada', 'Agendada'),
	# 	('Cancelada', 'Cancelada'),
	# 	('Espera', 'Espera'),
	# 	('Realizada', 'Realizada'),
	# )
    #Implementar STATUS NA CONSULTA SE TIVER TEMPO

    patient = models.ForeignKey(CustomUser, verbose_name="Paciente", on_delete=models.CASCADE, null=True)
    # day = models.DateTimeField(null=True, default=datetime.today)
    # hour = models.CharField(max_length= 10,verbose_name="Horário", choices=CHOICES, null=True)
    schedule = models.ForeignKey(Schedule, verbose_name="Agenda médica", on_delete=models.CASCADE, null=True)
    time_scheduled = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     if self.day is None:
    #         schedule = schedule.objects.get(pk=self.schedule.id)
    #         self.day = schedule.day.strftime(f'%Y-%m-%d {self.hour}')
    #     super(Exam, self).save(*args, **kwargs)

    # def specialty(self):
    #     return self.schedule.medical_name.specialty

    # def agenda(self):
        
    #     qs = Schedule.objects.filter(id=self.schedule)
    #     return qs
    #     agenda()
    def patient_name(self):
        return self.patient.username

    def __str__(self) -> str:
        return str(f'{self.patient.username} - {self.schedule}')

    class Meta:
        managed = True
        verbose_name= "Consulta"
        verbose_name_plural= 'Consultas'