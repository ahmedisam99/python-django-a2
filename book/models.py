from django.db import models
from user.models import User


class Book(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    pub_date = models.DateField(verbose_name="Publish Date")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
