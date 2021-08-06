from django.shortcuts import render
from .models import Student_Leads, Hunted_Leads,Employee
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import ListView,DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import Hunted_LeadSerializer, Student_LeadSerializer, EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

class StudentList(ListView):
    model = Student_Leads
    template_name = "base/home.html"
    context_object_name = 'student'

class StudentDetail(DetailView):
    model = Student_Leads
    template_name='base/student_details.html'
    context_object_name = 'student'



class StudentCreateView(CreateView):
    model = Student_Leads
    fields = "__all__"
    template_name = "base/create_student.html"
    success_url = reverse_lazy('home')



class StudentUpdateView(UpdateView):
    model = Student_Leads
    template_name = "base/update_student.html"
    fields = "__all__"
    success_url = reverse_lazy('home')


class StudentDeleteView(DeleteView):
    model = Student_Leads
    template_name = "base/delete_student.html"
    context_object_name = 'student'
    success_url = reverse_lazy('home')
#-----------------------------------------------#


class EmployeeList(ListView):
    model = Hunted_Leads
    template_name = "base/emp_home.html"
    context_object_name = 'employee'


class EmployeeDetail(DetailView):
    model = Hunted_Leads
    template_name = 'base/emp_details.html'
    context_object_name = 'employee'


class EmployeeCreateView(CreateView):
    model = Hunted_Leads
    fields = "__all__"
    template_name = "base/create_employee.html"
    success_url = reverse_lazy('emp_home')

    

class EmployeeUpdateView(UpdateView):
    model = Hunted_Leads
    template_name = "base/update_employee.html"
    fields = "__all__"
    success_url = reverse_lazy('emp_home')


class EmployeeDeleteView(DeleteView):
    model = Hunted_Leads
    template_name = "base/delete_employee.html"
    context_object_name = 'employee'
    success_url = reverse_lazy('emp_home')

    #___________________________________________#


@api_view()
def hunted_list(request):
    if request.method == 'GET':
        snippets = Hunted_Leads.objects.all()
        serializer = Hunted_LeadSerializer(snippets, many = True)
       # print(serializer)
        return Response(serializer.data)
