from django.urls import path, include
from django.views import View
from .import views


urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('editprofile', views.editprofile, name='editprofile'),
    path('changepassword', views.changepassword, name='changepassword'),
    

]
