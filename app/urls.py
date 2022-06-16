from django.urls import path
from . import views


urlpatterns = [
path('',views.show_app_page,name="show-app-page"),
path('query',views.render_pages,name="render_pages"),
]


