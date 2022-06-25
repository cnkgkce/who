from typing import Any
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import requests,logging,threading
from django.contrib import messages
import concurrent.futures
from .models import Site


"""
Bu dosya whatsmyname servisi olacak ve burada yer alan her bir fonksiyon ilgili sitede, hedef kullanıcı adının olup olmadığını
kontrol edecek ve bize ilgili web sitesinin linkini döndürecek

"""


class create_dict(dict):
    """
    Bu class'ı servis sonucunda çıktıları bir dictionary içerisinde toplamak istediğim için yazdım
    
    """
    def __init__(self):  # Classdan obje oluştuğunda init ile constructor çalışsın ve bana bir dictionary oluştursun
        self = dict()

    def add(self, key:str, value:Any):  # add metodu sayesinde verilen key değeri ve value ile match yapabiliriz
        self[key] = value

    def clear_dict(self):
        self.clear()


sites = create_dict()  # sites isimli dictionary yapısı tüm fonksiyonların çıktılarını toplayacak ve en sonunda results.html render edilirken template tarafına gönderilecek


# Create your views here.

@login_required(login_url='login-user')
def show_app_page(request):
    return render(request, "app/app.html")



thread_local = threading.local() # Her bir sessionda bir thread oluşturmak için bunu yapıyorum


def get_session() -> concurrent.futures:
    """
    Bu metod her bir servis içerisinde yeni bir session oluşturacak. requests'i session ile oluşturmak performans yönünden
    avantaj sağlıyor
    """

    if not hasattr(thread_local,"session"):
        thread_local.session = requests.Session()
    return thread_local.session



def create_site_object(slug:str,url:str) -> None:
    """
    Bu metod verilen slug ve url bilgisine göre önce bir Site objesi oluştur ardından bu objenin
    url değerini dışarıdan verilen url değeri ile değiştirip globalde yazılan sites:dict veri tipine ekleme yapar
    """
    site  = Site.objects.get(slug = slug)
    site.url = url
    site.save()
    sites.add(slug,site)



@login_required(login_url='login-user')
def get_github_account(request, username: str) -> None:
    """
    Eğer username'e ait bir hesap varsa ilgili username'e ait önce check işlemi ardından da profilin urlsini dict'a ekler
    Eğer username'e ait bir hesap yoksa None döndürür 

    """
    REQUEST_URL = f"https://api.github.com/users/{username}"
    try:
        session = get_session()
        with session.get(REQUEST_URL) as response:
            if response.status_code == 200:
                url = f"https://github.com/{username}"
                create_site_object('github',url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_producthunt_account(request, username: str) -> None:
    """
    Eğer username'e ait bir producthunt hesabı varsa onun bağlantısını gönderir, yoksa birşey döndürmez 

    """
    url = f"https://producthunt.com/@{username}"
    try:
        session = get_session()
        with session.get(url) as response:
            if response.status_code == 200:
                create_site_object('producthunt',url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_hackerone_account(request, username: str) -> None:
    url = f"https://hackerone.com/{username}?type=user"

    try:
        session = get_session()
        with session.get(url) as response:
            if response.status_code == 200:
                create_site_object('hackerone',url)
    except requests.Timeout as err:
        logging.error(err)



@login_required(login_url='login-user')
def get_bitbucket_account(request, username: str) -> None:
    url = f"https://bitbucket.org/{username}/"
    try:
        session = get_session()
        with session.get(url) as response:
            if response.status_code == 200:
                create_site_object('bitbucket',url)
    except requests.Timeout as err:
        logging.error(err)



@login_required(login_url='login-user')
def get_kik_account(request, username: str) -> None:
    url = f"https://ws2.kik.com/user/{username}"
    try:
        session = get_session()
        with session.get(url) as resp:
            if resp.status_code == 200:
                create_site_object('kik',url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_snapchat_account(request, username: str) -> None:
    url = f"https://snapchat.com/add/{username}"
    try:
        session = get_session()
        with session.get(url) as resp:
            if resp.status_code == 200:
                create_site_object('snapchat',url)
    except requests.Timeout as err:
        logging.error(err)



@login_required(login_url='login-user')
def get_codewars_account(request, username: str) -> None:
    url = f"https://codewars.com/users/{username}"
    try:
        session = get_session()
        with session.get(url) as resp:
            if resp.status_code == 200:
                create_site_object('codewars',url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_tiktok_account(request, username: str) -> None:
    url = f"https://tiktok.com/@{username}?lang=en"
    try:
        session = get_session()
        with session.get(url) as resp:
            if resp.status_code == 200:
                create_site_object('tiktok',url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_tradingview_account(request, username: str) -> None:
    url = f"https://tradingview.com/u/{username}/"
    try:
        session = get_session()
        with session.get(url) as resp:
            if resp.status_code == 200:
                create_site_object('tradingview',url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_youtube_account(request, username: str) -> None:
    url = f"https://youtube.com/user/{username}/videos"
    try:
        session = get_session()
        with session.get(url) as resp:
            if resp.status_code == 200:
                create_site_object('youtube',url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_kaggle_account(request, username: str) -> None:
    url = f"https://kaggle.com/{username}"
    try:
        session = get_session()
        with session.get(url) as resp:
            if resp.status_code == 200:
                create_site_object('kaggle',url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_tumblr_account(request, username: str) -> None:
    url = f"{username}.tumblr.com"
    try:
        session = get_session()
        with session.get(url) as resp:
            if resp.status_code == 200:
                create_site_object('tumblr',url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_wordpress_account(request, username) -> None:
    url = f"https://profiles.wordpress/{username}"
    try:
        session = get_session()
        with session.get(url) as resp:
            if resp.status_code == 200:
                create_site_object('wordpress',url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_reddit_account(request, username) -> None:
    """
    Bu metottan emin değilim bi test et
    
    """
    url = f"https://oauth.reddit.com/user/{username}/about.json?redditWebClient=desktop2x&app=desktop2x-client-production&gilding_detail=1&awarded_detail=1&raw_json=1"
    try:
        session = get_session()
        with session.get(url) as resp:
            if resp.status_code == 200:
                create_site_object('reddit',url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_fatsecret_account(request, username) -> None:
    url = f"https://www.fatsecret.com/member/{username}"
    try:
        session = get_session()
        with session.get(url) as resp:
            if resp.status_code == 200:
                create_site_object('fatsecret',url)
    except requests.Timeout as err:
        logging.error(err)

@login_required
def get_vsco_account(request,username) -> None:
    url = f"https://vsco.co/{username}/gallery"
    try:
        session = get_session()
        with session.get(url) as resp:
            if resp.status_code == 200:
                create_site_object('vsco',url)
    except requests.Timeout as err:
        logging.error(err)
    


@login_required(login_url='login-user')
def trigger(request):
    """
    trigger() fonksiyonu aslında formdan sadece bir defa username bilgisini alıp tüm servislere bunu paslayacak
    
    https://stackoverflow.com/questions/17601698/can-you-perform-multi-threaded-tasks-within-django
    üstteki linke bir bak 

    """
    username = str(request.POST['username'])

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.submit(get_github_account,request,username)
        executor.submit(get_producthunt_account,request,username)
        executor.submit(get_hackerone_account,request,username)
        executor.submit(get_bitbucket_account,request,username)
        executor.submit(get_kik_account,request,username)
        executor.submit(get_snapchat_account,request,username)
        executor.submit(get_codewars_account,request,username)
        executor.submit(get_tiktok_account,request,username)
        executor.submit(get_tradingview_account,request,username)
        executor.submit(get_youtube_account,request,username)
        executor.submit(get_kaggle_account,request,username)
        executor.submit(get_tumblr_account,request,username)
        executor.submit(get_wordpress_account,request,username)
        executor.submit(get_reddit_account,request,username)
        executor.submit(get_fatsecret_account,request,username)
        executor.submit(get_vsco_account,request,username)

@login_required(login_url='login-user')
def render_pages(request):
    if request.method == "GET":
        return render(request, "app/app.html")

    elif request.method == "POST":
        try:  # Diger tüm asenkron metotlar burada yer alacak
            trigger(request)
            return render(request, "app/results.html", {
                "sites": sites  # I'am genius broooo
            })
        except requests.exceptions.HTTPError as err:
            messages.error(request, "Bir hata oluştu lütfen tekrar deneyiniz...")
            raise SystemExit(err)
        finally:
            sites.clear_dict()
    else:
        return redirect("show-app-page")
