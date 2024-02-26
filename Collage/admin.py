from django.contrib import admin
from Collage.models import *
# Register your models here.



@admin.register(AnswerSheet)
class AnswerSheetAdmin(admin.ModelAdmin):
    list_display = ['dept',"subject","batch"]
    
@admin.register(StudentResultSheet)
class StudentResultSheetAdmin(admin.ModelAdmin):
    list_display = ['name',"roll"]
