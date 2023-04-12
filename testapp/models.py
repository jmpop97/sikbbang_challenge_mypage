from django.db import models

# Create your models here.
class TestApp(models.Model):
    class Meta:
        db_table="test_app"
    name = models.CharField(max_length=20)
    something = models.CharField(max_length=20)

    def __str__(self):
        return self.name
