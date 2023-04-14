from django.db import models
from user.models import UserModel


class QnaModel(models.Model):
    class Meta:
        db_table = "Qna_register"
    client = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    qna_title = models.CharField(max_length=30)
    qna_content = models.TextField(max_length=500)
    qna_created_at = models.DateTimeField(auto_now_add=True)
    qna_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
