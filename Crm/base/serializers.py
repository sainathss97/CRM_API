from .models import Hunted_Leads,Student_Leads,Employee
from rest_framework import serializers


class Student_LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Leads
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class Hunted_LeadSerializer(serializers.ModelSerializer):
    emp_details = EmployeeSerializer()
    stu_details = Student_LeadSerializer()
    class Meta:
        model = Hunted_Leads
        fields = "__all__"
