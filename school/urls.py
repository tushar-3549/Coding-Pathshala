from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # path("", views.student_list, name='student_list'),
    # path("add/", views.add_student, name="add_student"),
    # path('students/<str:slug>/', views.view_student, name='view_student'),
    # path('edit/<str:slug>/', views.edit_student, name='edit_student'),
    # path('delete/<str:slug>/', views.delete_student, name='delete_student'),

    path('notification/mark-as-read/', views.mark_notification_as_read, name='mark_notification_as_read'),
    path('notification/clear-all', views.clear_all_notification, name='clear_all_notification')


]