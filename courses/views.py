from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Course
from .forms import CourseForm
from enrollments.models import Enrollment


def course_list(request: HttpRequest) -> HttpResponse:
    courses = Course.objects.all()
    return render(request, 'courses/list.html', {'courses': courses})

def course_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()

    return render(request, 'courses/form.html', {'form': form})

def course_detail(request: HttpRequest, id: int) -> HttpResponse:
    course = get_object_or_404(Course, id=id)# bu ancha qulay ekan ancha qulay qulda error yozish ham shart emas

    enrollments = Enrollment.objects.filter(course=course)

    return render(
        request,
        'courses/detail.html',
        {
            'course': course,
            'enrollments': enrollments,
        }
    )

def course_delete(request: HttpRequest, id: int) -> HttpResponse:
    course = get_object_or_404(Course, id=id)

    enrollments = Enrollment.objects.filter(course=course)
    if enrollments.exists():
        error_message = "Bu kursda studentlar yozilgan. O‘chirish mumkin emas."
        return render(
            request,
            'courses/detail.html',
            {
                'course': course,
                'enrollments': enrollments,
                'error': error_message,
            }
        )

    course.delete()
    return redirect('course_list')