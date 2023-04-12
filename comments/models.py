from django.db import models
from users.models import UserModel


# Create your models here.
class CommentModel(models.Model):
    class Meta:
        db_table = "my_comment"

    comment_writer = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment_created_at = models.DateTimeField(auto_now_add=True)  # 이게 이미 날짜 찍는거
    comment_content = models.CharField(max_length=200)
    comment_image = models.ImageField(upload_to='')

# username = models.CharField(max_length=20, null=False)
# password = models.CharField(max_length=256, null=False)
# bio = models.CharField(max_length=256, default='')
# created_at = models.DataTimeField(auto_now_add=True)
# updated_at = models.DataTimeField(auto_now=True)
