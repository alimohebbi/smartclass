from django.shortcuts import render
from classroom.models import Classroom


def reserve(request, class_name):
    classroom = Classroom.objects.get(name=class_name)
    return render(request, 'reserve.html', {
        'schedule': classroom.schedule
    })


def report(request):
    return render(request, 'problem_report.html', {})


def room_view(request):
    return render(request, 'class-room.html', {})