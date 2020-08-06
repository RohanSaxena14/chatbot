from django.db import models

# Create your models here.
class queries(models.Model):
    question = models.CharField(max_length = 1000,null = True)
    answer = models.CharField(max_length = 1000,null = True)