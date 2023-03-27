from django.shortcuts import render
from django.shortcuts import render
# Create your views here.

def Index(request):
    return render(request,'Item/homepage.html')

def Contact(request):
    return render(request,'Item/contact.html')

def aboutus(request):
    return render(request,'Item/about.html')
