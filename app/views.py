from django.shortcuts import render

# Create your views here.


def show_app_page(request):
    return render(request,"app/app.html")