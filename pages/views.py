from django.shortcuts import redirect, render
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,"pages/index.html")


def show_about_page(request):
    return render(request,"pages/about.html")




def show_contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Bize ulaştığınız için teşekkür ederiz...")
            return redirect('show-contact-page')
    else:
        form = ContactForm()
    
    return render(request,'pages/contact.html',{'form' : form})


