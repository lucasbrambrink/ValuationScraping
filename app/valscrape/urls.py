from django.conf.urls import patterns, include, url
from django.contrib import admin
from valscrape.views import IndexView,AllView, GraphView, GenerateGraphView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'all$', AllView.as_view(), name='all'),
   	url(r'chart/(?P<data>[a-zA-Z]+)', GraphView.as_view(), name='graph'),
   	url(r'render/', GenerateGraphView.as_view(), name='render')
)