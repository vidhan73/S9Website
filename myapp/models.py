from django.db import models

class StudentRegistration(models.Model):
    Name = models.CharField(max_length=100)
    MobileNo = models.CharField(max_length=40)
    Class = models.CharField(max_length=30)
    Batch = models.TextField()
    Coupon = models.TextField()
   
def __str__(self):
     return self.Name

class StaffRegistration(models.Model):
    Name = models.CharField(max_length=100)
    MobileNo = models.CharField(max_length=40)
    Salary = models.CharField(max_length=30)
    Address = models.TextField()
    Courses = models.TextField()
   
def __str__(self):
     return self.Name
    
class ClassRecord(models.Model):
    Class = models.CharField(max_length=100)
    Batch = models.CharField(max_length=100)
    Board = models.CharField(max_length=100)
   
def __str__(self):
     return self.Class


class Staffattendance(models.Model):
    AdminName = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    MobileNo = models.CharField(max_length=100)
    Date = models.DateField()
    Course = models.CharField(max_length=100)
    Attendance = models.CharField(max_length=100)
 
def __str__(self):
     return self.Name

class Topper(models.Model):
    Name= models.CharField(max_length=100)
    Image= models.ImageField(upload_to='static/slider/',default='')
    Percentage= models.CharField(max_length=100)     
    Date= models.CharField(max_length=100)

def __str__(self):
     return self.Name    

class Class1(models.Model):
    Name= models.CharField(max_length=100)
    Batch=models.CharField(max_length=100)
    FatherName=models.CharField(max_length=100)
    School=models.CharField(max_length=300)

def __str__(self):
     return self.Name    

class igallery(models.Model):
    gname = models.CharField(max_length=400)
    gpic = models.ImageField(upload_to='static/gallery/',default='')
def __str__(self):
    return self.gname

class itopper(models.Model):
    gname = models.CharField(max_length=400)
    gpic = models.ImageField(upload_to='static/gallery/',default='')
def __str__(self):
    return self.gname

class ifestivals(models.Model):
    gname = models.CharField(max_length=400)
    gpic = models.ImageField(upload_to='static/gallery/',default='')
def __str__(self):
    return self.gname

class iinstitute(models.Model):
    gname = models.CharField(max_length=400)
    gpic = models.ImageField(upload_to='static/gallery/',default='')
def __str__(self):
    return self.gname

class salary(models.Model):
    name = models.CharField(max_length=400)
    salary=models.IntegerField(max_length=10)
    Date=models.DateField()
    Amount=models.IntegerField(max_length=10)
def __str__(self):
    return self.name  

class videonews(models.Model):
    vlink = models.CharField(max_length=500)
    vhead = models.CharField(max_length=500)
    vdate = models.DateField()

class Anotice(models.Model):
    notice = models.CharField(max_length=500)
    vdate = models.DateField()                              

def __str__(self):
    return self.notice
