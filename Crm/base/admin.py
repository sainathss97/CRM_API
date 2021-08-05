from django.contrib import admin
from .models import Employee, Student_Leads, Hunted_Leads
# Register your models here.
admin.site.register(Employee)
admin.site.register(Student_Leads)
admin.site.register(Hunted_Leads)
