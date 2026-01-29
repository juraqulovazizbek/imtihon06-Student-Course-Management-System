from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Course


def course_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'courses/list.html')

def course_create(request: HttpRequest) -> HttpResponse:
    return render(request, 'courses/form.html')

def course_detail(request: HttpRequest,  id: int) -> HttpResponse:
    return render(request, 'courses/detail.html')

def course_delete(request: HttpRequest, id: int) -> HttpResponse:
    return render(request, 'courses/detail.html')

