from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Tweet(models.Model):
    text = models.CharField(max_length=100)
    image = models.TextField()
    pub_date = models.DateTimeField('date publiched')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text