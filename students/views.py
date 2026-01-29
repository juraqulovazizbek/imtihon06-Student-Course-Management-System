from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.db.models import Q

from .models import Student
from .forms import StudentForm
from enrollments.models import Enrollment


def student_list(request: HttpRequest) -> HttpResponse:
    students = Student.objects.all()

    min_age = request.GET.get('min_age')
    if min_age:
        try:
            students = students.filter(age__gte=int(min_age))
        except ValueError:
            pass  

    search = request.GET.get('search')
    if search:
        students = students.filter(
            Q(full_name__icontains=search) | Q(email__icontains=search)
        )

    return render(request, 'students/list.html', {'students': students})


def student_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'students/form.html', {'form': form})


def student_detail(request: HttpRequest, id: int) -> HttpResponse:
    student = get_object_or_404(Student, id=id)

    enrollments = Enrollment.objects.filter(student=student).select_related('course')

    return render(
        request,
        'students/detail.html',
        {
            'student': student,
            'enrollments': enrollments,
        }
    )


def student_delete(request: HttpRequest, id: int) -> HttpResponse:
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return redirect('student_detail', id=student.id)
