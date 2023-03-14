from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    des = models.TextField()

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.TextField()
    pas = models.TextField()

    def __str__(self):
        return self.name
