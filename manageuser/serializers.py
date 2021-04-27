from rest_framework import serializers
from .models import Employee,Schedule

class EmployeeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','first_name','last_name','adm_priviledge','birthdate','schedule')

class ScheduleSerializer (serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id','horaires')