from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from valscrape.models import Companies,Stocks
import json
import os

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

## Write static file first ## this is obviously not a good way to do it,
## but I think it is worthy of employing good problem solving techniques. 

def write_graph_file(request):
	## parse the data ##




	## write to function-call to file ##
	file_names = os.listdir('valscrape/static/valscrape')
	pathname = os.path.join('valscrape/static/valscrape',file_names[3])
	graph = open(pathname, 'r').readlines()
	graph[31] = "stockBar(10,15,'no','yes')"
	graph_out = open(pathname, 'w')
	graph_out.writelines(graph)
	graph_out.close()
	print('all this is fine')
	return redirect('index')


