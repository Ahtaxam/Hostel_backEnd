from re import I
from django.contrib import admin
from .models import Employee, Expense, Room, Student, StudentsFee


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_no', 'no_of_beds', 'living_student', 'active']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'father_name', 'email', 'address',
                    'student_cnic', 'college_name', 'phone_no', 'room_no']


@admin.register(StudentsFee)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_no', 'date', 'fee']


@admin.register(Expense)
class Expense(admin.ModelAdmin):
    list_display = ['expense', 'price']


@admin.register(Employee)
class Employee(admin.ModelAdmin):
    list_display = ['employeeName', 'phoneNo',
                    'address', 'cnic', 'designation']
