from django.urls import path

from . import views


urlpatterns = [
    path('room', views.getRooms, name='rooms'),
    path('room/<str:pk>', views.getRoom, name='single_room'),
    path('create', views.createRoom, name='create_room'),
    path('update/<str:pk>', views.update_room, name='update_room'),
    path('delete/<str:pk>', views.delete_room, name='delete_room'),



    path('students', views.get_students, name='students'),
    path('registerstudent', views.add_student, name='registerstudent'),
    path('student/<str:pk>', views.get_student, name='student'),
    path('update_student/<str:pk>', views.update_student, name='update_student'),
    path('delete_student/<str:pk>', views.delete_student, name='delete_student'),



    path('fee', views.get_students_fee, name="StudentsFee"),
    path('addfee', views.add_student_fee, name='addfee'),

    # path('expenses', views.getExpenses, name="Expenses"),
    # path('addexpenses', views.addExpenses, name="add Expenses")

]
