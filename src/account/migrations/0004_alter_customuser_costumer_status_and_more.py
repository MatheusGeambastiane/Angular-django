# Generated by Django 4.0.4 on 2022-05-24 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_customuser_teste_customuser_costumer_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='costumer_status',
            field=models.BooleanField(default=False, help_text='Cliente padrão, poderá marcar consultas', verbose_name='Paciente'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='manager_status',
            field=models.BooleanField(default=False, help_text='Poderá criar agendas médicas', verbose_name='Gestor médico'),
        ),
    ]