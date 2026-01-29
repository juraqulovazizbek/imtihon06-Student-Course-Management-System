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
            return redirect('course_create')
        else:
            form = CourseForm()

    return render(request, 'courses/from.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Course
from enrollments.models import Enrollment


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
    return render(request, 'courses/detail.html')

