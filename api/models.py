from datetime import datetime
from django.db import models
# Create your models here.


class Room(models.Model):
    room_no = models.CharField(max_length=20)
    no_of_beds = models.CharField(max_length=20)
    living_student = models.IntegerField(default=0)
    active = models.BooleanField()

    def __str__(self):
        return self.room_no


class Student(models.Model):
    student_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=100)
    student_cnic = models.CharField(max_length=30)
    college_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=30)
    room_no = models.CharField(max_length=10)

    def __str__(self):
        return self.student_name


class StudentsFee(models.Model):
    name = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    fee = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Expense(models.Model):
    expense = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    # time = models.CharField(max_length=20)

    def __str__(self):
        return self.expense


class Employee(models.Model):
    employeeName = models.CharField(max_length=30)
    phoneNo = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    cnic = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)

    def __str__(self):
        return self.employeeName
