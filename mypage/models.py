from django.db import models
from qna.models import QnaModel
# Create your models here.
class MyPage(models.Model):
    class Meta:
        db_table="my_page"
    name = models.CharField(max_length=20)
    qna_key=models.ManyToManyField(QnaModel,blank=True,related_name='mypage_key')

    def __str__(self):
        return self.name