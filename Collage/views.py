from typing import Any
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.http import JsonResponse
import cv2
import numpy as np
from django.views.generic import ListView
from Collage.models import *
from .ImageProcessor.crop_sheet import crop_sheet
import base64
from django.contrib import messages
from Collage.forms import *
import pandas as pd
# Create your views here.


@login_required(login_url="/auth/login")
def home(request):
    
    return render(request,"index.html")





from Collage.ImageProcessor.calculator import calculate_imgage
class CreateTemplate(View):
    
    def get(self,request,*args, **kwargs):
        return render(request,"create-template.html")
    
    
    def calculator_result(self,exam_sheet,Archive_id):
        
        file = AnswerSheet.objects.get(pk=Archive_id).result_sheet
        ans_sheet = cv2.imdecode(np.frombuffer(file.read(), np.uint8),1)
        
        return calculate_imgage(ans_sheet,exam_sheet)
    
    
    def post(self,request,*args, **kwargs):
        if request.GET.get("img_lookUp"):
            context = {}
            
            file = request.FILES['file']
            
            img = cv2.imdecode(np.frombuffer(file.read(), np.uint8),1)
            
            
            if request.GET.get("result"):
                context , img = self.calculator_result(img, int(request.GET.get("Archive_id")) )
            
            else:
                
                img = crop_sheet(img)
            
            
            retval, buffer = cv2.imencode('.png', img)
            base64_img = base64.b64encode(buffer).decode()
            context.update({"img_b64":base64_img})

            return JsonResponse(context)
        
        form = AnswerSheetForm(request.POST,files=request.FILES)
        if form.is_valid():
            messages.success(request, "New Template Created.")
            form.save()
            return redirect("/")
        else:
            messages.error(request, "Invalid Form.")
            
        self.get(request,*args, **kwargs)
        
    


def about(request):
    return render(request,"about.html")



class Archive(ListView):
    queryset = AnswerSheet.objects.all().order_by("-pk")
    template_name = "Archive.html"
    


from django.http import HttpResponse
class StudentsList(ListView,View):
    queryset = StudentResultSheet.objects.all()
    template_name = "student-list.html"
    
    def get_queryset(self,*args, **kwargs):
        return AnswerSheet.objects.get(pk=self.kwargs['pk']).students.all()
    
    def get(self, request, *args, **kwargs):
        if request.GET.get("q"):

             data = {}
             for i in request.GET.get('q').split(','):
                 try:
                     data.update({i:None})
                 except:pass
             
             
             return self.download_csv(data.items())
             
        return super().get(request, *args, **kwargs)
    
    
    
    
    def get_context_data(self, **kwargs: Any) :
        context =  super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context
    
    def post(self,request,*args, **kwargs):
        
        post_data = dict(request.POST.copy())
        del post_data['csrfmiddlewaretoken']
        url = "-".join([key for key, val in post_data.items()])
   
        print(post_data.items())
        print(url)
        if request.GET.get("download"):
            
            
            link =  request.build_absolute_uri('/')[:-1] + "/download/"  + url +"/"
            print(link)
            
            return render(request,'share-download.html',{"link":link,"sms":"Student Results"})
        
        
        return redirect(f"/download/{url}/")
        
        
        
        



def studentDetails(request,pk):
    return render(request,"student.html",{
        "student":StudentResultSheet.objects.get(pk=pk),
        "prefix":"Details",
        "read_only":True
    })




class StudentAdd(View):
     
     
    def get(self,request,*args, **kwargs):
        return render(request,"student.html",{
            "prefix":"Add",
            "read_only":False,
            "pk":kwargs['pk']
        })
        
    
    def post(self,request,*args, **kwargs):
   

        form = StudentResultSheetForm(request.POST,files=request.FILES)
        if form.is_valid():
            messages.success(request, "New Student Created.")
            student= form.save()
            
            ans_room = AnswerSheet.objects.get(pk=kwargs['pk'])
            ans_room.students.add(student)
            ans_room.save()
            
             
            return redirect(f"/Archive/{kwargs['pk']}/students/")
        else:
            messages.error(request, "Invalid Form.")
            
        self.get(request,*args, **kwargs)
     
     

    







def downloadStudentResultSheet(request,slug):
        df = pd.DataFrame()
        
        for key in slug.split("-"):
            try:
                a = StudentResultSheet.objects.filter(pk=int(key)).values(
                    "name", "roll","physics","chemistry","math","english","analytical","result"
                )[0]
      
                df = df._append(a, ignore_index=True)
            except Exception as e:
                pass
              
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="student_result.csv"'
        df.to_csv(path_or_buf=response, index=False)  
        return response






from django.views.generic.edit import UpdateView 


def studentDetailsEdit(request,pk):
    item = StudentResultSheet.objects.get(pk=pk)

    print(request.POST)
    if request.method == 'POST':
        form = StudentResultSheetForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            
            print(request.POST)
    
    
    return redirect(f'/student-details/{pk}/')  
