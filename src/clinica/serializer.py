from asyncore import read
from pyexpat import model
from .models import Exam, Schedule, Medical, Specialty
from rest_framework import serializers

class TimeList(serializers.ListSerializer):
    def to_representation(self, data):
        now = datetime.now().strftime('15:00:00')
        return data.queryset.filter(horario__gte=now)

class TimeSerializer(serializers.ModelSerializer):
    hour = serializers.TimeField(format='%H:%M')

    class Meta:
        model = Exam
        fields = ('hour')

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model= Specialty
        fields= 'specialty_name'

class MedicalSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer(read_only=True)

    class Meta:
        model = Schedule
        fields = ('medical_name', 'crm', 'specialty')


class ScheduleSerializer(serializers.ModelSerializer):
    medical = MedicalSerializer(read_only=True)
    hours = serializers.SerializerMethodField('get_hours')

    def get_hours(self, ):
        now = datetime.now().strftime('%Y-%m-%d %H:%M')
        queryset = Schedule.objects.filter(schedule__id=schedule.id, day__gte=now, patient__isnull=True)
        serializer = TimeSerializer(instance=queryset, many=True)
        data = [hour.get('hour') for hour in serializer.data]
        return data

    class Meta:
        model = Schedule
        fields = ('day', 'hour', 'medical_name')

class ExamSerializer(serializers.ModelSerializer):
    medical = MedicalSerializer(read_only=True)

    def get_medical(self, exam):
        queryset = Medical.objects.get(pk=exam.schedule.medical_name.id)
        return MedicalSerializer(instance=queryset).data

    class Meta:
        model = Exam
        fields = ( 'day', 'hour', 'medical')





