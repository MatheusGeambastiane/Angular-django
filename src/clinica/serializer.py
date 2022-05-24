import imp
from .models import Exam, Schedule
from rest_framework import serializers

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

