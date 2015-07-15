from django.shortcuts import render

# Create your views here.


def about_us(request):
    return render(request, 'about_us.html')


def evaluation(request):
    return render(request, 'evaluation-merge.html')


def class_view(request):
    return render(request, 'class-room.html')


def dashboard_view(request):
    return render(request, 'dashboard.html')


def lost_view(request):
    return render(request, 'lost.html')


def teacher_poll_view(request):
    return render(request, 'teacher_poll.html')


def poll_view(request):
    return render(request, 'pollmerge.html')


def problem_report_view(request):
    return render(request, 'problem_report.html')


def reserve_view(request):
    return render(request, 'reserve.html')

def tracking_view(request):
    return render(request, 'tracking.html')


def student_enter_view(request):
    return render(request, 'student_enter.html')


def teacher_enter_view(request):
    return render(request, 'teacher_enter.html')


def messaging_view(request):
    return render(request, 'messaging.html')