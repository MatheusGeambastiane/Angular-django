from django.contrib import admin

from .models import (Medical, Exam, Schedule, Specialty, Hour)


@admin.register(Medical)
class MedicalAdmin(admin.ModelAdmin):
    list_display = ('name', 'crm', 'specialty')
    search_fields = ('name', 'specialty')
    list_filter = ('specialty',)

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('patient', 'specialty', 'schedule')
    search_fields = ('patient','specialty', 'schedule')
    list_filter = ('patient',)

 
#admin.site.register(Medical)

admin.site.register(Schedule)
admin.site.register(Specialty)
admin.site.register(Hour)

# Register your models here.
