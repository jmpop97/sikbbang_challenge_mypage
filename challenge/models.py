from django.db import models
from user.models import UserModel

# Create your models here.


class ChallengeModel(models.Model):
    class Meta:
        db_table = "challenges"

    challenge_author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    challenge_title = models.CharField(max_length=50)
    challenge_name = models.CharField(max_length=50)
    challenge_genre = models.CharField(max_length=50)
    challenge_content = models.TextField()
    challenge_image = models.ImageField(upload_to='', blank=True, null=True)
    challenge_created_at = models.DateTimeField(auto_now_add=True)
    challenge_updated_at = models.DateTimeField(auto_now=True)
