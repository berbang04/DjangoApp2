from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,"page/home_page.html",{})
def about(request):
    return render(request,"page/about.html",{})
def contact(request):
    return render(request,"page/contact.html",{})

# Create your views here.
