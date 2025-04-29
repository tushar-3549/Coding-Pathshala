
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.student_list, name='student_list'),
    # path('add/', views.add_student, name='add_student')
    path('add-student/', views.add_student, name='add-student')

]
