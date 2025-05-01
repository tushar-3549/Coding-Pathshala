
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add_student/', views.add_student, name='add_student'),
    path('view_student/<str:slug>/', views.view_student, name='view_student'),
    path('edit_student/<str:slug>/', views.edit_student, name='edit_student'),
    path('delete_student/<str:slug>/', views.delete_student, name='delete_student')

]
