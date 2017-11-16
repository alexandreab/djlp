from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)


class Discipline(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    unit = models.IntegerField(default=0)


class Program(models.Model):
    course = models.ForeignKey(Course)
    disciplines = models.ManyToManyField(Discipline)
