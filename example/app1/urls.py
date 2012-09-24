from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',

    url(r'^$', views.home, name='home'),
    url(r'^other/(?P<other_id>\d+)$', views.other, name='other'),
    url(r'^more/(?P<more_name>\w+)$', views.more, name='more'),
)
