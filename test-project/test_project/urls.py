from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/settings/', include('xlivesettings.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    url(r'^$', 'localsite.views.index')
)
