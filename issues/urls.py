from django.conf.urls import url

urlpatterns = [

    url(r'tracking/$', 'issues.views.tracking'),
    url(r'lost/$', 'issues.views.lost'),
    url(r'teacher-eval/$', 'issues.views.teacher_evaluation'),
    url(r'issue-eval/$', 'issues.views.issues_eval'),
    url(r'poll/$', 'issues.views.poll'),

]