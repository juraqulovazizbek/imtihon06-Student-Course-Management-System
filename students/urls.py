from django.urls import path

from .views import student_list, student_create, student_detail, student_delete


urlpatterns = [
    path('',student_list, name='student_list'),                 
    path('create/', student_create, name='student_create'),     
    path('<int:id>/',student_detail, name='student_detail'),  
    path('<int:id>/delete/',student_delete, name='student_delete'),
]
