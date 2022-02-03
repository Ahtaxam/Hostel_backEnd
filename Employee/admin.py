from django.contrib import admin
from django.db import models
from .models import Expense, Workers, WorkersPay
# Register your models here.


@admin.register(Workers)
class Workers(admin.ModelAdmin):
    list_display = ['workersName', 'phoneNo', 'address', 'cnic', 'designation']


@admin.register(WorkersPay)
class WorkersPayment(admin.ModelAdmin):
    list_display = ['name', 'phone_no', 'date', 'payment']


@admin.register(Expense)
class Expense(admin.ModelAdmin):
    list_display = ['expense', 'date', 'price']
