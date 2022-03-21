from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api/get_quiz/', views.get_quiz, name="get_quiz")
]
