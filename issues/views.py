from django.shortcuts import render


def tracking(request):
    return render(request, 'tracking.html', {})


def lost(request):
    return render(request, 'lost.html', {})


def teacher_evaluation(request):
    return render(request, 'teacher_poll.html')


def issues_eval(request):
    return render(request, 'evaluation-merge.html', {})


def poll(request):
    return render(request, 'pollmerge.html', {})
