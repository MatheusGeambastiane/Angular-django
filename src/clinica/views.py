
#django
from datetime import datetime
from django.shortcuts import render
#My APPS
from .serializer import ExamSerializer, ScheduleSerializer, TimeList, TimeSerializer, MedicalSerializer, SpecialtySerializer
from .models import Exam, Schedule, Medical, Specialty

#3rd Party

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter



class SpecialtyViewSet(ReadOnlyModelViewSet):
    serializer_class = SpecialtySerializer
    queryset = Specialty.objects.all()
    search_fields = ('specialty_name')
    filter_backends = (OrderingFilter, SearchFilter)
    permission_classes = (IsAuthenticated,)
    

class MedicalViewSet(ReadOnlyModelViewSet):
    serializer_class = MedicalSerializer
    queryset = Medical.objects.all()
    search_fields = ('medical_name', 'crm')
    filter_backends = (OrderingFilter, SearchFilter)
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        specialty = self.request.query_params.getlist('specialty')
        queryset = self.queryset

        if specialty:
            return queryset.filter(specialty__id=specialty)
        return queryset



class ScheduleViewSet(ReadOnlyModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
    search_fields = ('medical_name')
    filter_backends = (OrderingFilter, SearchFilter)
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        queryset = self.queryset
        medical = self.request.query_params.getlist('medical')
        today = datetime.now()
        specialty = self.request.query_params.getlist('specialty')
        day = self.request.query_params.getlist('day')

        if medical:
            queryset.filter(medical__id__in=medical)
        if specialty:
            queryset.filter(medical__specialty__id__in=specialty)

        if day:
            queryset.filter(day__gte=today.strftime('%Y - %m - %d'))


        return queryset





class ExamViewSet(ModelViewSet):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    search_fields = ('schedule', 'day')
    filter_backends = (OrderingFilter, SearchFilter)
    permission_classes = (IsAuthenticated,)
    allowed_methods = ('GET', 'POST', 'DELETE')


    # def create(self, request, *args, **kwargs):
    #     exam = request.data.get
    #     exa = Exam.objects.create(
    #         patient_id = self.request.user.id,
    #         schedule_id=self.request.data.schedule.id)
    #     exa.save(force_insert=False)
    #     serializer = ExamSerializer(exa)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


    # def get_queryset(self):
    #     return Exam.objects.filter(patient=self.request.user)

    # def create(self, request, *args, **kwargs):

    #     exam_id = request.data.get('exam_id')
    #     exam = Exam.objects.create(id=exam_id, hour=request.data.get('hour'))
    #     exam.patient = self.request.user
    #     exam.save(*args, **kwargs)
    #     serializer = ExamSerializer(exam)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


    def destroy(self, request, *args, **kwargs):
        if Exam.objects.filter(id=kwargs['pk'], done=False, patient=request.user):
            return self.destroy(self,*args, **kwargs)
        else:
            return Response({
            'msg' : 'Não foi possível desmarcar esta consulta.',
            'status': status.HTTP_204_NO_CONTENT
            })




# Create your views here.
