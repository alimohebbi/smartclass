from django.conf.urls import include, url, static
from django.contrib import admin
from portal import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'portal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^about_us/$', 'smartclass.views.about_us'),
    url(r'^evaluation/$', 'smartclass.views.evaluation'),
    url(r'^class_room/$', 'smartclass.views.class_view'),
    url(r'^dashboard/$', 'smartclass.views.dashboard_view'),
    url(r'^lost/$', 'smartclass.views.lost_view'),
    url(r'^teacher_poll/$', 'smartclass.views.teacher_poll_view'),
    url(r'^teacher/$', 'smartclass.views.teacher_poll_view'),
    url(r'^poll/$', 'smartclass.views.poll_view'),
    url(r'^problem_report/$', 'smartclass.views.problem_report_view'),
    url(r'^reserve/$', 'smartclass.views.reserve_view'),
    url(r'^student_enter/$', 'smartclass.views.student_enter_view'),
    url(r'^teacher_enter/$', 'smartclass.views.teacher_enter_view'),
    url(r'^tracking/$', 'smartclass.views.tracking_view'),
    url(r'^messaging/$', 'smartclass.views.messaging_view'),

]
# + static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)