from django.db import models

# Create your models here.


class Challenge(models.Model):
    class Meta:
        db_table = "challenges"

    # challenge_writer = ''
    chellenge_title = models.CharField(max_length=50)
    challenge_name = models.CharField(max_length=50)
    challenge_genre = models.CharField(max_length=50)
    challenge_content = models.TextField()
    challenge_image = models.ImageField(upload_to='', blank=True, null=True)
    challenge_created_at = models.DateTimeField(auto_now_add=True)
    challenge_updated_at = models.DateTimeField(auto_now=True)
