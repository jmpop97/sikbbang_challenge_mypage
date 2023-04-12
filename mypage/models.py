from django.db import models
from testapp.models import TestApp
# Create your models here.
class MyPage(models.Model):
    class Meta:
        db_table="my_page"
    name = models.CharField(max_length=20)
    mypage_test=models.ManyToManyField(TestApp,blank=True,related_name='testname')

    def __str__(self):
        return self.name