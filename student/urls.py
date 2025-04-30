
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add_student/', views.add_student, name='add_student'),
    path('students/<str:slug>/', views.view_student, name='view_student'),
    # path('student/edit/<int:pk>/', views.edit_student, name='edit_student'),


]
