from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('delete/<int:pk>/',views.delete_task,name="delete"),
    path('finish/<int:pk>/',views.finish_task,name="change_status")
]