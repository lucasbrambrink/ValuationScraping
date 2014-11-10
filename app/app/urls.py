from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'valscrape.views.root', name='root'),
    url(r'^valscrape/', include('valscrape.urls', namespace='valscrape', app_name='valscrape')),
    url(r'^formula/', include('formula.urls', namespace='formula', app_name='formula')),
    url(r'^report/', include('interactive_annual_report.urls', namespace='report', app_name='iar')),
)
