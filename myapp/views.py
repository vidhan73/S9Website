from django.shortcuts import render,redirect
import requests
from .models import *


def index(request):
    data =Topper.objects.all()
    ndata= Anotice.objects.all()
    mydict={"img":data,"n":ndata}
    return render(request,"user/index.html",context=mydict)

def image(request):
    d=igallery.objects.all().order_by('-id')
    mydict={"data":d}
    return render(request, 'user/image.html',context=mydict)

def AdminDashboard(request):
    return render(request, 'admin/dashboard.html')   

def Student(request):
    data = ClassRecord.objects.all()
    mydict={"class":data}
    return render(request, 'admin/studentregistration.html',context=mydict)

def StudentRecord(request):
    data = StudentRegistration.objects.all()
    
    mydict={"sr":data}
    return render(request, 'admin/StudentRecord.html',context=mydict)

def Staff(request):
    return render(request,'admin/StaffRegistration.html')   

def StaffRecord(request):
    data = StaffRegistration.objects.all()
    mydict={"t":data}
    return render(request, 'admin/StaffRecord.html',context=mydict)        

def Classes(request):
    data = ClassRecord.objects.all()
    print(data)
    mydict={"cr":data}
    return render(request, 'admin/StaffRecord.html',context=mydict) 

def delete(request,id):
    data= ClassRecord.objects.get(id=id)
    data.delete()
    return redirect("/dashboared/studentrecored/")

def edit(request):
    class1= Class1.objects.all()
    mydict={"c1":class1}
    return redirect("/dashboard/ClassRecord",context=mydict)      

def contactus(request):
    return render(request,'user/contactus.html')  

def aboutus(request):
    return render(request,'user/aboutus.html')  

def attendance(request):
    return render(request,'admin/attendance.html')

def staffattendance(request):
    data = StaffRegistration.objects.all()
    mydict={"sd":data}
    return render(request,'admin/staffattendance.html',context=mydict)            

def CourseRegistration(request):
    return render(request,'admin/CoursesRegistration.html')    

def class1(request):
    return render(request,'admin/1to8.html')        

def salary(request):
    data = StaffRegistration.objects.all()
    mydict={"t":data}
    return render(request,'admin/salary.html',context=mydict)    

def StudentAttendance(request):
    data= ClassRecord.objects.all()       
    sdata= StudentRegistration.objects.all()
    mydict={"class":data,"student":sdata}
    return render(request,'admin/studentAttendance.html',context=mydict)    

def message(request):
    return render(request,'admin/message.html') 

def fees(request):
    data= ClassRecord.objects.all()       
    sdata= StudentRegistration.objects.all()
    mydict={"class":data,"student":sdata}
    return render(request,'admin/fees.html',context=mydict)   

def video(request):
    from django.db.models import Q
    vd = videonews.objects.all().order_by('-id')
    mydict = {"vdata":vd}
    return render(request, 'user/video.html',mydict)         
