from django.conf.urls import *

urlpatterns = patterns('xlivesettings.views',
    (r'^$', 'site_settings', {}, 'site_live_settings'),
    (r'^export/$', 'export_as_python', {}, 'settings_export'),
    (r'^(?P<group>[^/]+)/$', 'group_settings'),
)
