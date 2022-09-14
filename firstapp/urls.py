from django.urls import path, include
from django.views import View
from .import views


urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.index, name='index'),
]