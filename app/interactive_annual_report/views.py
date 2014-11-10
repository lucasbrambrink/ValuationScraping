from django.shortcuts import render
from django.views.generic.base import View
from . import models
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'interactive_annual_report/index.html')


class GetAnnualReportView(View):

    def get(self, request, *args, **kwargs):
        stock = models.Stock.objects.get(symbol=request.GET.get('symbol', ''))
        annual_report = stock.annualreport_set.filter(stock=stock, year=request.GET.get('year', '')).values()
        #response = serializers.serialize('json', annual_report)
        response = [ar for ar in annual_report]
        data = {
            'name': stock.name,
            'symbol': stock.symbol,
            'annualReport': response
        }
        return JsonResponse(data)

class GetKeyStaticsView(View):

    def get(self, request, *args, **kwargs):
        key_statics = models.KeyStatics.objects.filter(annual_report=self.kwargs['report_id']).values()
        response = [res for res in key_statics]
        data = {
            'key_statics': response
        }
        return JsonResponse(data)
