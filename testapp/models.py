from django.db import models
# Create your models here.

class Products(models.Model):

    class Meta:
        db_table="products"

    name = models.CharField(max_length=20)
    code = models.BigAutoField(primary_key=True)
    description = models.TextField()
    prise = models.PositiveBigIntegerField()
    amount= models.PositiveBigIntegerField()
    sizes =(('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),)
    size=models.CharField(choices=sizes, max_length=1)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.code

    def __str__(self):
        return self.name