from django.db import models
from testapp.models import Products
# Create your models here.

class Mypage(models.Model):
    class Meta:
        db_table = "my_page"

    userkey = models.ManyToManyField(Products,blank=True,related_name='Products')