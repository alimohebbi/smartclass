from django.shortcuts import render


def messages(request):
    return render(request, 'messaging.html', {})


def teacher_sign_in(request):
    return render(request, 'teacher_enter.html', {})


def student_sign_in(request):
    return render(request, 'student_enter.html', {})


def dashboard(request):
    return render(request, 'dashboard.html', {})