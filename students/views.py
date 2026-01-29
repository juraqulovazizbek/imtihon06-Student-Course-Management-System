from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def student_list(request: HttpRequest) -> HttpResponse:
     return render(request, 'students/list.html')

def student_create(request: HttpRequest) -> HttpResponse:
    return render(request, 'students/form.html')

def student_detail(request: HttpRequest, id: int) -> HttpResponse:
      return render(request, 'students/detail.html')

def student_delete(request: HttpRequest, id:int) -> HttpResponse:
    return render(request, 'courses/detail.html')
