from pyexpat import model
from django.db import models

# Create your models here.


class Workers(models.Model):
    workersName = models.CharField(max_length=30)
    phoneNo = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    cnic = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)

    def __str__(self):
        return self.workersName


class WorkersPay(models.Model):
    name = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    payment = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Expense(models.Model):
    expense = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    price = models.CharField(max_length=30)

    def __str__(self):
        return self.expense
