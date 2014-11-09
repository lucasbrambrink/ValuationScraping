from django.conf.urls import patterns, include, url
from django.contrib import admin
from valscrape.views import IndexView,AllView, GraphView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'all$', AllView.as_view(), name='all'),
   	url(r'chart/(?P<data>[a-zA-Z]+)','valscrape.views.write_graph_file', name='graph')
)