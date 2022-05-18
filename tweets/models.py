from django.db import models

# Create your models here.

class Tweet(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=100)
    image = models.TextField()
    pub_date = models.DateTimeField('date publiched')

    def __str__(self):
        return self.text