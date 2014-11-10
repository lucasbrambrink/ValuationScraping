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
		print('hello')
		all_companies = Companies.objects.all()
		print(all_companies)
		company_array = []
		for company in all_companies:
			company_array.append(company.symbol)
		return JsonResponse({'companies' : company_array})

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

def write_graph_file(request,data):
	## parse the data ##
	company = Companies.objects.get(symbol=data)
	stock = Stocks.objects.filter(company_id=company.id)[0]
	
	chart_labels = ["PE","EV / EBITDA", "EV / Revenue", "Debt / Equity", "Return on Equity", " Free Cash / Revenue"]
	chart_data = [round(float(stock.trailing_pe),3),
		round(float(stock.EV_EBITDA),3),
		round(float(stock.EV_revenue),3),
		round(float(stock.total_debt_equity[:-1]),3),
		round(float(stock.return_on_equity[:-1]),3),
		round(float(stock.levered_free_cash_flow[:-1]),3)/round(float(stock.revenue[:-1]),3)]
	chart_average = calculate_average()
	## calculate percent difference ## 





	## build line
	line = "radarChart(["
	i = 0
	while i < len(chart_labels):
		line += "'"+str(chart_labels[i])+"'"
		if i+1 != len(chart_labels):
			line += ","
		i += 1
	line += "],["
	i = 0
	while i < len(chart_data):
		line += str(round(chart_data[i],3))
		if i+1 != len(chart_data):
			line += ","
		i += 1
	line += "],["
	i = 0
	while i < len(chart_average):
		line += str(round(chart_average[i],3))
		if i+1 != len(chart_average):
			line += ","
		i += 1
	line += "])"
	print(line)

	## write to function-call to file ##
	file_names = os.listdir('valscrape/static/valscrape')
	print(file_names)
	pathname = os.path.join('valscrape/static/valscrape',file_names[4])
	graph = open(pathname, 'r').readlines()
	graph[122] = line
	graph_out = open(pathname, 'w')
	graph_out.writelines(graph)
	graph_out.close()
	return render(request, 'valscrape/bar.html', {'company' : company})

def calculate_average():
	all_companies = Companies.objects.all()
	N = len(all_companies)
	all_stocks = Stocks.objects.all()
	average_pe = 0
	average_EV_ebitda = 0
	average_EV_revenue = 0
	average_debt_equity = 0
	average_return_equity = 0
	average_cash_revenue = 0
	for stock in all_stocks:
		average_pe += round(float(stock.trailing_pe),3)
		average_EV_ebitda += round(float(stock.EV_EBITDA),3)
		average_EV_revenue += round(float(stock.EV_revenue),3)
		average_debt_equity += round(float(stock.total_debt_equity[:-1]),3)
		average_return_equity += round(float(stock.return_on_equity[:-1]),3)
		if stock.revenue == "0":
			average_cash_revenue = 0
		else:
			average_cash_revenue += round(float(stock.levered_free_cash_flow[:-1]),3)/round(float(stock.revenue[:-1]),3)
	average_pe /= N
	average_EV_ebitda /= N
	average_EV_revenue /= N
	average_debt_equity /= N
	average_return_equity /= N
	average_cash_revenue /= N
	average = [average_pe,average_EV_ebitda,average_EV_revenue,average_debt_equity,average_return_equity,average_cash_revenue]
	return average

