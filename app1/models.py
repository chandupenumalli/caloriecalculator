from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(primary_key=True,max_length=50)
    password=models.CharField(max_length=10)
    desig=models.CharField(max_length=15,default="user")
    def __str__(self):
        return self.email
class Message(models.Model):
    name=models.CharField(max_length=50)
    Phone=models.CharField(primary_key=True,max_length=10,default="")
    email=models.CharField(max_length=50)
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.email