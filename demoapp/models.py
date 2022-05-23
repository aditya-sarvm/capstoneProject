from django.db import models

# Create your models here.
class Recommendations(models.Model):
    title = models.CharField(max_length=50)
    popularity = models.IntegerField()