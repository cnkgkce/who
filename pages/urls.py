from django.urls import path
from . import views

urlpatterns = [
path('',views.index,name="index"),
path('index/',views.index),
path('about/',views.show_about_page,name="show-about-page"),
path('contact/',views.show_contact_page,name="show-contact-page"),
]
