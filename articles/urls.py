from django.contrib import admin
from django.urls import path,include
from . import views


#nepton,nepton,nepton,...
app_name = "nep_blog"
urlpatterns = [
    path('articles/', views.ar_list),
    path('articles/<slug:slug>', views.page),
    path('', views.home,name="home"),
    path('post/<slug:slug>', views.post ,name="post"),
    path('about-me/', views.about),
]
