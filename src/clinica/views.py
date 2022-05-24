from django.shortcuts import render

from .serializer import ExamSerializer
from .models import Exam
#3rd Party
from rest_framework import viewsets



class ExamViewSet(viewsets.ModelViewSet):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()

# Create your views here.
