from django.urls import path, include
from django.views import View
from .import views


urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('editprofile', views.editprofile, name='editprofile'),
    path('changepassword', views.changepassword, name='changepassword'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('userpro', views.userpro, name='userpro'),
    path('userpro', views.userpro, name='userpro'),
    path('editauth',views.editauth, name='editauth'),
    path('changepasswordauth',views.changepasswordauth, name='changepasswordauth'),
]
