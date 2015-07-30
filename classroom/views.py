from django.shortcuts import render

# Create your views here.


def reserve(request):
    return render(request, 'reserve.html', {})


def report(request):
    return render(request, 'problem_report.html', {})


def room_view(request):
    return render(request, 'class-room.html', {})