from django.db import models


# Create your models here.

class BookModel(models.Model):
    name=models.CharField(max_length=250)
    author=models.CharField(max_length=250)
    profile=models.ImageField(upload_to="images",null=True,blank=True)
    category=models.CharField(max_length=200)
    description=models.CharField(max_length=250)

    def __str__(self):
        return self.name

