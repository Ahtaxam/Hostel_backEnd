from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Expense, Room, Student, StudentsFee
from .serializers import ExpenseSerializer, RoomSerializers, StudentFeeSerializers, StudentSerializers
from api import serializers


@api_view(["GET"])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializers(rooms, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getRoom(request, pk):
    rooms = Room.objects.get(room_no=pk)
    serializer = RoomSerializers(rooms, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def update_room(request, pk):
    try:
        room = Room.objects.get(room_no=pk)
        serializer = RoomSerializers(instance=room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def createRoom(request):
    data = request.data
    room = Room.objects.create(
        room_no=data['room_no'], no_of_beds=data['no_of_beds'], active=data['active']
    )
    serializer = RoomSerializers(room, many=False)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_room(request, pk):
    room = Room.objects.get(room_no=pk)
    room.delete()
    return Response("Deleted Successfully")


#               Views for Student Model


@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    serializer = StudentSerializers(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_student(request, pk):
    students = Student.objects.get(phone_no=pk)
    serializer = StudentSerializers(students, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_student(request):
    data = request.data
    student = Student.objects.create(
        student_name=data['student_name'], father_name=data['father_name'], email=data['email'], address=data['address'], student_cnic=data[
            'student_cnic'], college_name=data['college_name'], phone_no=data['phone_no'], room_no=data['room_no']
    )
    serializer = StudentSerializers(data=student)
    if serializer.is_valid():
        serializer.save()
    return Response("Added Successfully")


@api_view(['PUT'])
def update_student(request, pk):
    student = Student.objects.get(phone_no=pk)
    serializer = StudentSerializers(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Updated Successfully !!")


@api_view(['DELETE'])
def delete_student(request, pk):
    student = Student.objects.get(phone_no=pk)
    student.delete()
    return Response("Deleted Successfully!")


#                   Views for Fee Models


@api_view(['GET'])
def get_students_fee(request):
    students = StudentsFee.objects.all()
    serializer = StudentFeeSerializers(students, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_student_fee(request):
    data = request.data
    fee = StudentsFee.objects.create(
        name=data['name'], phone_no=data['phone_no'],
        date=data['date'], fee=data['fee']
    )
    serializer = StudentSerializers(data=fee)
    if serializer.is_valid():
        serializer.save()
    return Response("Added Successfully")


#                       Views For Expenses


@api_view(['GET'])
def getExpenses(request):
    expenses = Expense.objects.all()
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addExpenses(request):
    data = request.data
    expense = Expense.objects.create(
        expense=data['expense'], price=data['price']
    )
    serializer = ExpenseSerializer(data=expense)
    if serializer.is_valid():
        serializer.save()
    return Response("Added Successfully")


#                   Views For Employees
