from django.conf.urls import url

urlpatterns = [
    url(r'reserve/$', 'classroom.views.reserve'),
    url(r'report/$', 'classroom.views.report'),
    url(r'(?P<room_id>\d+)/$', 'classroom.views.room_view'),
]