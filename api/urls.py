from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('get_task/',views.get_task),
    path('add_task/',views.add_task),
    path('delete_task/<str:pk>/',views.delete_task),
    path('update/<str:pk>/',views.update_task),
    
]