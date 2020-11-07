from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.TextField(null=False)
    author_name = models.TextField(null=False)
    publish_date = models.DateField()
