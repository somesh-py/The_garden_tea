from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages

# Create your views here.


def home(request):
    item = product.objects.all()
    return render(request,'home.html',{'item':item})


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def contactus(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        # aboutinfo.objects.create(name=name,email=email,subject=subject,messaage=message)
        aboutinfo.objects.create(name=name,email=email,subject=subject,messaage=message)
        messages.success(request,'your feedback reached sucessfully to us. thanks')
        return redirect('/contact/')
    