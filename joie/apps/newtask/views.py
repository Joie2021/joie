from django.shortcuts import render

# Create your views here.

def newtask(request):
    return render(request,'newtask/newtask.html')