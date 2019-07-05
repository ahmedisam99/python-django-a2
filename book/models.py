from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    category = models.CharField(max_length=20)
    status = models.CharField(max_length=8)
    available = models.BooleanField('Is the book available?')
    pub_date = models.DateField('Publish Date of the book')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
