from os import name
from django.urls import path

from . import views
urlpatterns = [
    path('employeerecord', views.get_Employee, name="employee record"),
    path('addemployee', views.add_employee, name='Add New Employee'),
    path('updateworker/<str:pk>', views.update_worker, name='update Worker'),
    path('deleteworker/<str:pk>', views.delete_worker, name='delete worker'),
    path('employeeid/<str:pk>', views.get_Employee_id, name="Unique Employee"),


    path('getpayment', views.get_payment, name="Get Payment"),
    path('paypayment', views.pay_payment, name="Pay Payment"),


    path('expenses', views.expenses, name='Expenses'),
    path('addexpense', views.add_expenses, name='Add Expense')
]
