from typing import Any
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"pages/index.html")


def show_about_page(request):
    return render(request,"pages/about.html")


def show_contact_page(request):
    return render(request,"pages/contact.html")
 




