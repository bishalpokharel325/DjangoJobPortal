from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Job(models.Model):
    position_name = models.CharField(max_length=150)
    created_at = models.DateField()
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    salary = models.IntegerField()
    no = models.IntegerField()
    description = RichTextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.position_name
