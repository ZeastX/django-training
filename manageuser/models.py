from django.db import models

# Create your models here.

class Schedule (models.Model):
    horaires = models.CharField(max_length=200)
    def __str__(self):
        return self.horaires

class Employee (models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    adm_priviledge = models.BooleanField()
    birthdate = models.DateField()
    schedule = models.ManyToManyField(Schedule)
    def __str__(self):
        return self.frist_name + self.last_name



