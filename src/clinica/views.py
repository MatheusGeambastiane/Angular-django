from django.shortcuts import render

from .serializer import ExamSerializer, ScheduleSerializer
from .models import Exam, Schedule
#3rd Party
from rest_framework import viewsets, status
from rest_framework.response import Response



class ExamViewSet(viewsets.ModelViewSet):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    allowed_methods = ('GET', 'POST', 'DELETE')


    def create(self, request, *args, **kwargs):
        exam = Exam.objects.get(_id=request.data.get(_id))
        exam.day
        return



    def destroy(self, request, *args, **kwargs):
        if Exam.objects.filter(id=kwargs['pk'], done=False, patient=request.user):
            return self.destroy(self,*args, **kwargs)
        else:
            return Response({
            'msg' : 'Não foi possível desmarcar esta consulta.',
            'status': status.HTTP_204_NO_CONTENT
            })


class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
    


# Create your views here.
