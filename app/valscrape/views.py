from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from valscrape.models import Companies,Stocks

# Create your views here.

class IndexView(View):
	template = 'valscrape/index.html'
	def get(self, request):
		return render(request, self.template)

class AllView(View):

	def post(self,request):
		return redirect('index')

	def get(self,request):
		all_companies = Companies.objects.all()
		company_array = []
		for company in all_companies:
			company_array.append(company.symbol)
		return JsonResponse({'stocks' : company_array})

class GraphView(View):
	template = 'valscrape/bar.html'

	def get(self,request):
		return render(request, self.template)

	def post(self,request):
		pass