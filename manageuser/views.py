from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,ListModelMixin,UpdateModelMixin,DestroyModelMixin
from .models import Employee,Schedule
from .serializers import EmployeeSerializer,ScheduleSerializer

# Create your views here.

class EmployeeViewset(GenericViewSet,CreateModelMixin,RetrieveModelMixin,ListModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ScheduleViewset(GenericViewSet,CreateModelMixin,RetrieveModelMixin,ListModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer