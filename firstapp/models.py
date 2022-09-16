from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class signup(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    username=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.IntegerField()
 