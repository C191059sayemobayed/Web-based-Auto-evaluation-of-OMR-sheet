from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class StudentResultSheet(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    roll = models.IntegerField(null=True,blank=True)
    
    
    exam_sheet = models.ImageField(upload_to="student/",null=True,blank=True)
    matched_sheet_b64 = models.TextField(null=True,blank=True)
    
    physics = models.IntegerField(null=True,blank=True,default=0)
    chemistry = models.IntegerField(null=True,blank=True,default=0)
    math = models.IntegerField(null=True,blank=True,default=0)
    english = models.IntegerField(null=True,blank=True,default=0)
    analytical = models.IntegerField(null=True,blank=True,default=0)
    result = models.IntegerField(null=True,blank=True,default=0)
    
    def __str__(self) -> str:
        return f"{self.name}-{self.roll}"

    def save(self, *args, **kwargs):
        total = 0
        
        if self.physics:
            total += self.physics
        if self.chemistry:
            total += self.chemistry
        if self.math:
            total += self.math
        if self.analytical:
            total += self.analytical
        if self.english:
            total += self.english
        
        self.result = total
        
        return super().save(*args, **kwargs)

class AnswerSheet(models.Model):
    subject = models.CharField(max_length=50,null=True,blank=True)
    dept = models.CharField(max_length=50,null=True,blank=True)
    batch = models.IntegerField(null=True,blank=True)
    examiner = models.CharField(max_length=50,null=True,blank=True)
    code = models.CharField(max_length=10,null=True,blank=True)
    students = models.ManyToManyField(StudentResultSheet,blank=True)
    result_sheet = models.ImageField(upload_to="result/",null=True,blank=True)
    
    def __str__(self) -> str:
        return f"{self.dept}-{self.batch} {self.subject}"
    
    
