from django.db import models

# Create your models here.
class Article(models.Model):

    blogtitle = models.CharField(max_length=100)
    blogauthor = models.CharField(max_length=100)
    blogcontent = models.TextField()
    publishdate = models.DateField()
    blogcategory = models.CharField(max_length=100)

