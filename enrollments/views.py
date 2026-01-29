from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def enrollment_create(request: HttpRequest) -> HttpResponse:
    return render(request, 'enrollments/form.html')

def enrollment_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'enrollments/list.html')