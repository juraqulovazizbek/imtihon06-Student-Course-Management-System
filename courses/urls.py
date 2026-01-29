from django.urls import path
from .views import course_list, course_create, course_detail, course_delete

urlpatterns = [
    path('',course_list, name='course_list'),                 
    path('create/', course_create, name='course_create'),     
    path('<int:id>/',course_detail, name='course_detail'),  
    path('<int:id>/delete/',course_delete, name='course_delete'),
]
