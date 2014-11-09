from django.conf.urls import patterns, include, url
from django.contrib import admin
from valscrape.views import IndexView,AllView, GraphView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'all$', 'valscrape.views.write_graph_file', name='all'),
    url(r'get', GraphView.as_view(), name='individual_graph'),
)
