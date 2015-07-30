from django.conf.urls import url

urlpatterns = [

    url(r'messages/$', 'users.views.messages'),
    url(r'teacher-login/$', 'users.views.teacher_sign_in'),
    url(r'student-login/$', 'users.views.student_sign_in'),
    url(r'dashboard/$', 'users.views.dashboard'),

]