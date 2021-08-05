from django.urls import path
from . import views
urlpatterns = [
    path('', views.StudentList.as_view(), name='home'),
    path('student/<int:pk>/',views.StudentDetail.as_view() ,name ='details'),
    path('create_stu/', views.StudentCreateView.as_view(), name='create_stu'),
    path('update_stu/<int:pk>/',views.StudentUpdateView.as_view(),name='update_stu'),
    path('delete_stu/<int:pk>/',views.StudentDeleteView.as_view(),name='delete_stu'),
    #--------------------------------------------

    path('emp_home', views.EmployeeList.as_view(), name='emp_home'),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view(), name='employee_details'),
    path('create_emp/', views.EmployeeCreateView.as_view(), name='create_emp'),
    path('update_emp/<int:pk>/',
         views.EmployeeUpdateView.as_view(), name='update_emp'),
    path('delete_emp/<int:pk>/',
         views.EmployeeDeleteView.as_view(), name='delete_emp'),
#_________________________________________________________________#

    path('api/', views.hunted_list,name ='api')
]
