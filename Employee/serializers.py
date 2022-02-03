from dataclasses import fields
from rest_framework import serializers
from.models import Expense, Workers, WorkersPay


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = ['workersName', 'phoneNo', 'address', 'cnic', 'designation']


class WorkersPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkersPay
        fields = ['name', 'phone_no', 'date', 'payment']


class HostelExpense(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['expense', 'date', 'price']
