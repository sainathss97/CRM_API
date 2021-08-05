from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Employee(models.Model):
    

    emp_name = models.ForeignKey(User,  on_delete=models.CASCADE)
    assigin = models.BooleanField(default = False)

    
    def __str__(self):
        return str(self.emp_name)


class Student_Leads(models.Model):

    stu_name = models.CharField(max_length=50)
    course_name = models.CharField(max_length=500)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.stu_name 

class Hunted_Leads(models.Model):
    emp_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    stu_name = models.ForeignKey(Student_Leads, on_delete=models.CASCADE)
    def __str__(self):
        return str(str(self.stu_name.stu_name)+"  Assigined to  "+str(self.emp_name.emp_name) )

    
