
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
    queryset = Specialty.objects.all()
    search_fields = ('specialty_name')
    filter_backends = (OrderingFilter, SearchFilter)
    permission_classes = (IsAuthenticated)

class MedicalViewSet(ReadOnlyModelViewSet):
    queryset = Medical.objects.all()
    search_fields = ('medical_name')
    filter_backends = (OrderingFilter, SearchFilter)
    permission_classes = (IsAuthenticated)


    def get_queryset(self):
        specialty = self.request.query_params.get_list('specialty')
        queryset = self.queryset

        if specialty:
            return queryset.filter(specialty__id=specialty)
        return queryset



class ScheduleViewSet(ReadOnlyModelViewSet):
    queryset = Schedule.objects.all()
    search_fields = ('medical_name')
    filter_backends = (OrderingFilter, SearchFilter)
    permission_classes = (IsAuthenticated)


    def get_queryset(self):
        queryset = self.queryset
        medical = self.request.query_params.get_list('medical')
        today = datetime.now()
        specialty = self.request.query_params.get_list('specialty')
        day = self.request.query_params.get_list('day')

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
    search_fields = ('medical_name')
    filter_backends = (OrderingFilter, SearchFilter)
    permission_classes = (IsAuthenticated)
    allowed_methods = ('GET', 'POST', 'DELETE')


    # def create(self, request, *args, **kwargs):
    #     exam = request.data.get
    #     exa = Exam.objects.create(
    #         medical =exam.schedule.medical_name,
    #         day= exam.schedule.day,
    #         hour= exam.schedule.schedule,
    #         schedule_id=request.data.get('schedule_id'))
    #     exam.save(force_insert=True)
    #     return

    def get_queryset(self):
        return Exam.objects.filter(patient=self.request.user)

    def create(self, request, *args, **kwargs):
        exam = Exam.objects.get(exam_id=request.data.get('exam_id'), hour=request.data.get('hour'))
        exam.patient = self.request.user
        exam.save(*args, **kwargs)
        serializer = ExamSerializer(exam)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def destroy(self, request, *args, **kwargs):
        if Exam.objects.filter(id=kwargs['pk'], done=False, patient=request.user):
            return self.destroy(self,*args, **kwargs)
        else:
            return Response({
            'msg' : 'Não foi possível desmarcar esta consulta.',
            'status': status.HTTP_204_NO_CONTENT
            })




# Create your views here.
