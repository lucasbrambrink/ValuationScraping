from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from valscrape.models import Companies,Stocks

# Create your views here.

class IndexView(View):
	template = 'valscrape/index.html'
	def get(self, request):
		return render(request, self.template)

	def post(self,request):
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
		name_value = []
		all_stocks = Stocks.objects.all()
		for stock in all_stocks:
			company = Companies.objects.get(id=int(stock.company_id))
			name_value_pair = (company.name,stock.trailing_pe)
			name_value.append(name_value_pair)
		return JsonResponse({'pe': name_value})

	def post(self,request):
		return render(request, self.template)

class TryView(View):
	template = 'valscrape/index.html'

	def get(self,request):
		new_string = "helo alksdjflakd  "
		return render(request, self.template)