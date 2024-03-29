from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from valscrape.models import Companies,Stocks
import json
import os

# Create your views here.


class IndexView(View):
	template = 'valscrape/root.html'
	def get(self, request):
		return render(request, self.template)

	def post(self,request):
		return render(request, self.template)

class PolarView(View):
	template = 'valscrape/all_polar.html'
	def get(self, request):
		all_companies = Companies.objects.all()
		lines = []
		for company in all_companies:
			chart_labels,chart_data,delta_data,chart_average = parse_data(company.symbol)
			target = ":"+company.name
			lines.append(build_line("polarArea",chart_labels,delta_data,target))
		write_to_file(lines)

		return render(request, self.template, {'companies': all_companies})



class AllView(View):

	def post(self,request):
		return redirect('index')

	def get(self,request):
		all_companies = Companies.objects.all()
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

def parse_data(data):
	## parse the data ##
	company = Companies.objects.get(symbol=data)
	stock = Stocks.objects.filter(company_id=company.id)[0]
	
	chart_labels = ["PE","EV / EBITDA", "EV / Revenue", "Debt / Equity", "Return on Equity", " Free Cash / Revenue"]
	chart_data = [round(float(stock.trailing_pe),3),
		round(float(stock.EV_EBITDA),3),
		round(float(stock.EV_revenue),3),
		round(float(stock.total_debt_equity[:-1]),3),
		round(float(stock.return_on_equity[:-1]),3),
		round(round(float(stock.levered_free_cash_flow[:-1]),3)/round(float(stock.revenue[:-1]),3),3)]
	chart_average = calculate_average()
	## calculate percent difference ## 
	delta_data = []
	print(chart_average)
	print(chart_data)
	i = 0
	while i < len(chart_data):
		if chart_average[i] == 0:
			delta = 0
		else:
			delta = (chart_data[i] - chart_average[i]) / chart_average[i] ## this returns a percent difference from average
		delta_data.append(round(delta,3))
		i += 1
	return(chart_labels,chart_data,delta_data,chart_average)



def build_line(chart_type,chart_labels,chart_data,chart_average):
	## build line
	line = chart_type+"Chart(["
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
	line += "]"

	if chart_average == "Null":
		line += ")"
		return line
	if chart_average[0] == ":":
		line += ","
		line += chart_average[1:]
		line += ")"
		return line
	line += ",["
	i = 0
	while i < len(chart_average):
		line += str(round(chart_average[i],3))
		if i+1 != len(chart_average):
			line += ","
		i += 1
	line += "])"
	return line

def write_to_file(lines):
	## write to function-call to file ##
	file_names = os.listdir('valscrape/static/valscrape')
	pathname = os.path.join('valscrape/static/valscrape',file_names[3])
	graph = open(pathname, 'r').readlines()
	i = 122
	for line in lines:
		graph[i] = line
		i += 1
	graph_out = open(pathname, 'w')
	graph_out.writelines(graph)
	graph_out.close()
	return True
	##return render(request, 'valscrape/bar.html', {'company' : company})

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
			average_cash_revenue += 0
		else:
			average_cash_revenue += round(float(stock.levered_free_cash_flow[:-1]),3)/round(float(stock.revenue[:-1]),3)
	average_pe /= N
	average_EV_ebitda /= N
	average_EV_revenue /= N
	average_debt_equity /= N
	average_return_equity /= N
	average_cash_revenue /= N
	average = [round(average_pe,3),round(average_EV_ebitda,3),round(average_EV_revenue,3),round(average_debt_equity,3),round(average_return_equity,3),round(average_cash_revenue,3)]
	return average

