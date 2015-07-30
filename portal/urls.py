from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic.base import TemplateView

from users import urls as users_urls
from issues import urls as issues_urls
from classroom import urls as class_urls


urlpatterns = [

    url(r'^accounts', include(users_urls)),
    url(r'^issues/', include(issues_urls)),
    url(r'^classroom/', include(class_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', TemplateView.as_view(template_name='about_us.html')),

]