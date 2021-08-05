from .models import Hunted_Leads,Student_Leads,Employee
from rest_framework import serializers


class Student_LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Leads
        fields = ('stu_name')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('emp_name')

class Hunted_LeadSerializer(serializers.ModelSerializer):
    emp_name = EmployeeSerializer
    stu_name = Student_LeadSerializer
    class Meta:
        model = Hunted_Leads
        fields = ['emp_name', 'stu_name']
