from pickle import TRUE
from django.shortcuts import render
from django.urls.conf import include

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Expense, Workers, WorkersPay
from .serializers import HostelExpense, WorkerSerializer, WorkersPaySerializer


@api_view(['GET'])
def get_Employee(request):
    employees = Workers.objects.all()
    serializer = WorkerSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_Employee_id(request, pk):
    employees = Workers.objects.get(phoneNo=pk)
    serializer = WorkerSerializer(employees, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_employee(request):
    data = request.data
    employee = Workers.objects.create(
        workersName=data['workersName'], phoneNo=data['phoneNo'],
        address=data['address'], cnic=data['cnic'], designation=data['designation']
    )

    serializer = WorkerSerializer(data=employee)
    if serializer.is_valid():
        serializer.save()
    return Response("Added Successfully !!")


@api_view(['PUT'])
def update_worker(request, pk):
    worker = Workers.objects.get(phoneNo=pk)
    serializer = WorkerSerializer(instance=worker, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Updated Successfully !!")


@api_view(['DELETE'])
def delete_worker(request, pk):
    worker = Workers.objects.get(phoneNo=pk)
    worker.delete()
    return Response("Deleted Successfully!")


#                   Workers Pay Views

@api_view(['GET'])
def get_payment(request):
    payment = WorkersPay.objects.all()
    serializer = WorkersPaySerializer(payment, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def pay_payment(request):
    data = request.data
    payment = WorkersPay.objects.create(
        name=data['name'], phone_no=data['phone_no'], date=data['date'], payment=data['payment']
    )
    serializer = WorkersPaySerializer(data=payment)
    if(serializer.is_valid()):
        serializer.save()
    return Response("Payment Paid ")


#                   Expense Views


@api_view(['GET'])
def expenses(request):
    expenses = Expense.objects.all()
    serializer = HostelExpense(expenses, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_expenses(request):
    data = request.data
    expenses = Expense.objects.create(
        expense=data['expense'], date=data['date'], price=data['price']
    )

    serializer = HostelExpense(data=expenses)
    if serializer.is_valid():
        serializer.save()
    return Response("Expense Added !")
