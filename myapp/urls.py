from django.urls import path
from . import views

urlpatterns = [
     path('index/', views.index),
     path('image/',views.image),
     path('dashboared/studentregistartion/',views.Student),
     path('dashboared/studentrecored/',views.StudentRecord),
     path('dashboared/staffregistartion/',views.Staff),
     path('dashboared/staffrecored/',views.StaffRecord),
     path('delete/<int:id>',views.delete),
     path('edit/',views.edit),
     path('contactus/',views.contactus),
     path('aboutus/',views.aboutus),
     path('attendance/',views.attendance),
     path('courseRegistration/',views.CourseRegistration),
     path('attendance/staffattendance/',views.staffattendance),
     path('class1/',views.class1),
     path('staffSalary/',views.salary),
     path('studentAttendance/',views.StudentAttendance),
     path('message/',views.message),
     path('fees/',views.fees),
     path('video/', views.video),
    
]