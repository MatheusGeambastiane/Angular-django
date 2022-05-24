from pyexpat import model
from .models import Exam, Schedule
from rest_framework import serializers

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    # schedule = ScheduleSerializer(many=True,read_only=False, required=False)
    class Meta:
        model = Exam
        # fields = '__all__'
        fields = ['patient', 'medical', 'specialty', 'schedule','done', 'day', 'hour', 'status']


