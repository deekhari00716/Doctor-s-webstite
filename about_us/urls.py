from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'about_us'

urlpatterns = [
    path('', views.about_us, name='about_us'),


]
