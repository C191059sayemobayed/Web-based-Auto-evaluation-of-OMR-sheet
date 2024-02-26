
from django.urls import path
from Auth.views import *
urlpatterns = [
    path('login/', login_user),
    path('singup/', signup),
    path('logout/', logout_user),
]