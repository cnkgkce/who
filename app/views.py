from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import requests,logging



"""
Bu dosya whatsmyname servisi olacak ve burada yer alan her bir fonksiyon ilgili sitede, hedef kullanıcı adının olup olmadığını
kontrol edecek ve bize ilgili web sitesinin linkini döndürecek

"""



class create_dict(dict):
    """
    Bu class'ı servis sonucunda çıktıları bir dictionary içerisinde toplamak istediğim için yazdım
    
    """
    def __init__(self):  #Classdan obje oluştuğunda init ile constructor çalışsın ve bana bir dictionary oluştursun
        self = dict()

    def add(self,key,value):  # add metodu sayesinde verilen key değeri ve value ile match yapabiliriz
        self[key] = value

    def clear(self):
        self.clear()


links = create_dict()  #links isimli dictionary yapısı tüm fonksiyonların çıktılarını toplayacak ve en sonunda results.html render edilirken template tarafına gönderilecek



# Create your views here.

@login_required(login_url='login-user')
def show_app_page(request):
    return render(request,"app/app.html")



def get_github_account(request):
    """
    Eğer username'e ait bir hesap varsa ilgili username'e ait önce check işlemi ardından da profilin urlsini dict'a ekler
    Eğer username'e ait bir hesap yoksa None döndürür 

    """
    username = str(request.POST['username'])
    print(username)
    REQUEST_URL = f"https://api.github.com/users/{username}"

    resp = requests.get(REQUEST_URL)
    if resp.status_code == 200:
        link = f"https://github.com/{username}"
        links.add("github",link)
        links.clear()
        return


def render_pages(request):
    if request.method == "GET":
        return render(request,"app/app.html")

    elif request.method == "POST":
        get_github_account(request)
        return render(request,"app/results.html",links)
        
    else:
        return redirect("show-app-page")

 




