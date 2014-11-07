from django.conf.urls import patterns, include, url
from django.contrib import admin
from valscrape.views import IndexView,AllView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'all$', AllView.as_view(), name='all'),
)
