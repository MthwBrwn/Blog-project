from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blogpage-home'),
    path('about/', views.about, name='blogpage-about')
]