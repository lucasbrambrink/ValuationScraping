from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^api/get$', views.GetAnnualReportView.as_view(), name='get'),
    url(r'^api/statics/(?P<report_id>[0-9]+)$', views.GetKeyStaticsView.as_view(), name='statics')
)