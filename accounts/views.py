from email import message
from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.


def redirect_user_accounts(request):
    """
    Bu fonksiyon kullanıcının oturumunun olup olmama durumuna göre kullanıcıyı yönlendirmek amacıyla yazılmıştır.
    Eğer kullanıcının oturumu yok ise kullanıcı otomatik olarak account/register endpointine yönlendirilir.
    Eğer kullanıcının oturumu varsa bu sefer dashboard'a yönlendirilir.

    """
    
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return render(request,"accounts/register.html")




def register_user(request):
    """
    Bu fonksiyon aldığı request type'ına göre ya register.html'i render eder ya da register.html içerisinde gönderilen form bilgileriyle bir kullanıcıyı kayıt eder
    
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                messages.success(request,"Kullanıcı Oluşturuldu!")
                return redirect('login-user')
        messages.warning(request,"Başarısız Kayıt İşlemi")
    
    form = RegisterForm()

    return render(request,"accounts/register.html",{"form" : form})



def login_user(request):
    """
    Bu fonksiyon aldığı request type'Ina göre ya login.html'i render eder ya da register.html içerisinde gönderilen form bilgileriyle bir kullanıcıyı kayıt eder
    """

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            #authenticate process
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username = username,password = password)
            if user is not None: #Yani kullanıcı varsa login yaptır
                login(request,user)
                return redirect('index')
            else:
                messages.warning(request,"Kullanıcı adı veya parola hatalı !")
                return redirect('login-user')
    else:
       form = LoginForm()
    
    return render(request,"accounts/login.html",{"form" : form})




def logout_user(request):
    """
    Bu fonksiyon kullanıcının oturumunu sonlandırır

    """
    logout(request)
    return redirect('index')

