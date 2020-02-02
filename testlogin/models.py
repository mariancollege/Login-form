from django.db import models

# Create your models here.
class logclass(models.Model):
    uname=models.TextField(max_length=20)
    pswd1=models.TextField(max_length=20)
    pswd2 = models.TextField(max_length=20)