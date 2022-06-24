import logging
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import requests
from django.contrib import messages

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

    def add(self, key, value):  # add metodu sayesinde verilen key değeri ve value ile match yapabiliriz
        self[key] = value

    def clear_dict(self):
        self.clear()


links = create_dict()  # links isimli dictionary yapısı tüm fonksiyonların çıktılarını toplayacak ve en sonunda results.html render edilirken template tarafına gönderilecek


# Create your views here.

@login_required(login_url='login-user')
def show_app_page(request):
    return render(request, "app/app.html")


# Buradan itibaren çalışan servisler yer alacak


@login_required(login_url='login-user')
def get_github_account(request, username: str) -> None:
    """
    Eğer username'e ait bir hesap varsa ilgili username'e ait önce check işlemi ardından da profilin urlsini dict'a ekler
    Eğer username'e ait bir hesap yoksa None döndürür 

    """
    REQUEST_URL = f"https://api.github.com/users/{username}"
    try:
        resp = requests.get(REQUEST_URL)
        if resp.status_code == 200:
            print("github request başarılı")
            link = f"https://github.com/{username}"
            links.add("github", link)
    except requests.Timeout as err:
        print("Github patladı")
        logging.error(err)


@login_required(login_url='login-user')
def get_producthunt_account(request, username: str) -> None:
    """
    Eğer username'e ait bir producthunt hesabı varsa onun bağlantısını gönderir, yoksa birşey döndürmez 

    """

    url = f"https://producthunt.com/@{username}"
    try:

        resp = requests.get(url)

        if resp.status_code == 200:
            links.add("producthunt", url)
    except requests.Timeout as err:
        print("Producthunt patladı")
        logging.error(err)


@login_required(login_url='login-user')
def get_hackerone_account(request, username: str) -> None:
    url = f"https://hackerone.com/{username}?type=user"
    try:

        resp = requests.get(url)
        if resp.status_code == 200:
            links.add("hackerone", url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_bitbucket_account(request, username: str) -> None:
    url = f"https://bitbucket.org/{username}/"
    try:

        resp = requests.get(url)
        if resp.status_code == 200:
            links.add("bitbucket", url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_kik_account(request, username: str) -> None:
    url = f"https://ws2.kik.com/user/{username}"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            links.add("kik", url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_snapchat_account(request, username: str) -> None:
    url = f"https://snapchat.com/add/{username}"
    try:

        r = requests.get(url)

        if r.status_code == 200:
            links.add("snapchat", url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_codewars_account(request, username: str) -> None:
    url = f"https://codewars.com/users/{username}"
    try:

        r = requests.get(url)

        if r.status_code == 200:
            links.add("codewars", url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_tiktok_account(request, username: str) -> None:
    url = f"https://tiktok.com/@{username}?lang=en"
    try:

        r = requests.get(url)

        if r.status_code == 200:
            links.add("tiktok", url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_tradingview_account(request, username: str) -> None:
    url = f"https://tradingview.com/u/{username}/"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            links.add("tradingview", url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_youtube_account(request, username: str) -> None:
    url = f"https://youtube.com/user/{username}/videos"
    try:

        r = requests.get(url)

        if r.status_code == 200:
            links.add("youtube", url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_kaggle_account(request, username: str) -> None:
    url = f"https://kaggle.com/{username}"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            links.add("kaggle", url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_tumblr_account(request, username: str) -> None:
    url = f"{username}.tumblr.com"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            links.add("tumblr", url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_wordpress_account(request, username) -> None:
    url = f"https://profiles.wordpress/{username}"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            links.add("wordpress", url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_reddit_account(request, username) -> None:
    """
    Bu metottan emin değilim bi test et
    
    """
    url = f"https://oauth.reddit.com/user/{username}/about.json?redditWebClient=desktop2x&app=desktop2x-client-production&gilding_detail=1&awarded_detail=1&raw_json=1"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            links.add("reddit", url)
    except requests.Timeout as err:
        logging.error(err)


@login_required(login_url='login-user')
def get_fatsecret_account(request, username) -> None:
    url = f"https://www.fatsecret.com/member/{username}"
    try:
        r = request.get(url)
        if r.status_code == 200:
            links.add("fatsecret", url)
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

    # get_github_account(request, username)

    # get_producthunt_account(request, username)

    # get_hackerone_account(request, username)

    # get_bitbucket_account(request, username)

    # get_kik_account(request, username)

    # get_snapchat_account(request, username)

    # get_codewars_account(request, username)

    # get_tiktok_account(request, username)

    # get_tradingview_account(request, username)

    # get_youtube_account(request, username)
    # time.sleep(5)
    # get_kaggle_account(request, username)
    # time.sleep(5)
    # get_tumblr_account(request, username)
    # time.sleep(5)
    # get_wordpress_account(request, username)
    # time.sleep(5)
    # get_reddit_account(request, username)
    # time.sleep(5)
    # get_fatsecret_account(request, username)
    # time.sleep(5)


@login_required(login_url='login-user')
def render_pages(request):
    if request.method == "GET":
        return render(request, "app/app.html")

    elif request.method == "POST":
        try:  # Diger tüm asenkron metotlar burada yer alacak
            trigger(request)
            return render(request, "app/results.html", {
                "links": links  # I'am genius broooo
            })
        except requests.exceptions.HTTPError as err:
            messages.error(request, "Bir hata oluştu lütfen tekrar deneyiniz...")
            raise SystemExit(err)
        finally:
            links.clear_dict()
    else:
        return redirect("show-app-page")
