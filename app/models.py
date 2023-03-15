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


class Note(models.Model):
    notes = models.TextField(max_length=100, blank=True)
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.notes


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title
