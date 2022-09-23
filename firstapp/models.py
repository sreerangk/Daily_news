from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_tbl(models.Model):
    uname=models.CharField(max_length=200)
    uemail=models.EmailField()
    uage=models.IntegerField()



class u_dp(models.Model):
    userdt=models.OneToOneField(User,on_delete=models.CASCADE)
    dp=models.ImageField(upload_to='user_dp/',null=True,blank=True)
    Address=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    addedon=models.DateTimeField(auto_now_add=True)
    updatedon=models.DateTimeField(auto_now=True)
    contact_no=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.userdt
