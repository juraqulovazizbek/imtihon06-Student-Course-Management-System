from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .forms import EnrollmentForm
from .models import Enrollment



def enrollment_list(request: HttpRequest) -> HttpResponse:
    enrollments = Enrollment.objects.all()
    return render( request, 'enrollments/list.html', {'enrollments': enrollments})

def enrollment_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
            form = EnrollmentForm()

    return render(request, 'enrollments/form.html', {'form': form})
    
