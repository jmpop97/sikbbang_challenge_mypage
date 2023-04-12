from django.db import models
from testapp.models import TestApp
# Create your models here.
class MyPage(models.Model):
    class Meta:
        db_table="my_page"
    testkey=models.ManyToManyField(TestApp,blank=True)