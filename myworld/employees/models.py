from django.db import models

class Employees(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  salary = models.IntegerField(25) 