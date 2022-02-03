from django.db import models
from .models import Employee, Room, Student, StudentsFee, Expense
from rest_framework import fields, serializers


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_no', 'no_of_beds', 'living_student', 'active']


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_name', 'father_name', 'email', 'address',
                  'student_cnic', 'college_name', 'phone_no', 'room_no']


class StudentFeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentsFee
        fields = ['name', 'phone_no', 'date', 'fee']


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['expense', 'price']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employeeName', 'phoneNo', 'address', 'cnic', 'designation']
