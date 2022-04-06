from django.db import models

# Create your models here.
    
class Book(models.Model):
    bid = models.CharField(max_length=20)
    bname = models.CharField(max_length=20)
    aname = models.CharField(max_length=20)
    categ = models.CharField(max_length=20)
    class Meta:
        db_table = "book"
    