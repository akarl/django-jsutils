from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'', include('example.app1.urls', namespace='app1')),
    url(r'^app2/', include('example.app2.urls', namespace='app2')),
)
