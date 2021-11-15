from django.urls import path
from django.conf import  settings
from . import views

app_name="newtask"

urlpatterns = [
    path('',views.newtask,name="newtask")
]
