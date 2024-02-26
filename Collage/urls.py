from django.urls import path
from Auth.views import *
from Collage.views import *

urlpatterns = [
    path("",home),
    path('create-template/', CreateTemplate.as_view()),
    path('about/', about),
    path('Archive/', Archive.as_view()),
    path('Archive/<int:pk>/students/', StudentsList.as_view()),
    path('student-details/<int:pk>/', studentDetails),
    path('Archive/<int:pk>/students/add/', StudentAdd.as_view()),
    path('download/<str:slug>/',downloadStudentResultSheet),
    path('student-details/<int:pk>/update/', studentDetailsEdit),
]
