from django.urls import path
from .views import enrollment_create, enrollment_list


urlpatterns = [
    path('',enrollment_list, name='enrollment_list'),                 
    path('create/', enrollment_create, name='enrollment_create'),     
]
