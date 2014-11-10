from django.shortcuts import render
from django.views.generic.base import View
from . import models
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


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
