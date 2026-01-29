from students.models import Student
from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import messages

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

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)

    students = Student.objects.filter(enrollment__course=course).distinct()
    enrollments = Enrollment.objects.filter(course=course).select_related('student')
    students_count = enrollments.count()

    context = {
        "course": course,
        "students": students,          # <-- TEMPLATE UCHUN SHU KERAK
        "enrollments": enrollments,    # (xohlasang qoldir)
        "students_count": students_count,
    }
    return render(request, "courses/detail.html", context)  # <-- TEMPLATE NOMI
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

def course_edit(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully.")
            return redirect("course_detail", pk=course.id)
    else:
        form = CourseForm(instance=course)

    return render(
        request,
        "courses/form.html",
        {
            "form": form,
            "course": course,
        },
    )

