from django.contrib import admin
from  .models import *

class studentregistration(admin.ModelAdmin):
    list_display = ('Name','MobileNo','Class','Batch','Coupon')

admin.site.register(StudentRegistration,studentregistration)

class staffregistration(admin.ModelAdmin):
    list_display = ('Name','MobileNo','Salary','Address','Courses')

admin.site.register(StaffRegistration,staffregistration)

class classes(admin.ModelAdmin):
    list_display = ('id','Class','Batch','Board')

admin.site.register(ClassRecord,classes)

class staffattendance(admin.ModelAdmin):
    list_display = ('id','AdminName','Date','Name','MobileNo','Course','Attendance')

admin.site.register(Staffattendance,staffattendance)

class topper(admin.ModelAdmin):
    list_display = ('id','Name','Image','Percentage','Date')

admin.site.register(Topper,topper)

class class1(admin.ModelAdmin):
    list_display = ('id','Name','Batch','FatherName','School')

admin.site.register(Class1,class1)

class igalleryAdmin(admin.ModelAdmin):
    list_display = ('id','gname','gpic')

admin.site.register(igallery,igalleryAdmin)

#class ifestivalAdmin(admin.ModelAdmin):
#    list_display = ('id','gname','gpic')

#admin.site.register(igallery,igalleryAdmin)

#class iinstituteAdmin(admin.ModelAdmin):
 #   list_display = ('id','gname','gpic')

#admin.site.register(igallery,igalleryAdmin)

#class itoppersAdmin(admin.ModelAdmin):
 #   list_display = ('id','gname','gpic')

#admin.site.register(igallery,igalleryAdmin)

class salaryAdmin(admin.ModelAdmin):
    list_display = ('id','name','salary','Date','Amount')

admin.site.register(salary,salaryAdmin)

class videonewsAdmin(admin.ModelAdmin):
    list_display = ('id','vlink','vhead','vdate')
admin.site.register(videonews,videonewsAdmin)

class notice(admin.ModelAdmin):
    list_display = ('id','notice','vdate')
admin.site.register(Anotice,notice)





