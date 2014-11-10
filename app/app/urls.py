from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^', include('valscrape.urls'), name='root'),
    url(r'^valulation', include('valscrape.urls'), name='index'),
    url(r'^formula', include('formula.urls'), name='index'),
    url(r'^report', include('interactive_annual_report.urls'), name='index')
)
