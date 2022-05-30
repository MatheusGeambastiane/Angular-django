# Generated by Django 4.0.4 on 2022-05-30 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0007_rename_email_medical_medical_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='day',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='hour',
        ),
        migrations.AddField(
            model_name='schedule',
            name='hour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='clinica.hour', verbose_name='horário'),
        ),
    ]
