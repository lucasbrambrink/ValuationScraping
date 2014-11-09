
##set up environment in script
import sys, os
sys.path.append('/app')
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
from django.conf import settings

import requests
import datetime
import time
import random
import bs4
import json
import re
from valscrape.models import Stocks,Companies

import django
django.setup()



## Scrape Yahoo Finance for Stock Information ##

class Finance_API:
	def __init__(self):
		self.base_link = 'http://finance.yahoo.com/q/ks?s='
		self.end_link = '+Key+Statistics'
		self.company_array = Companies.objects.all()

	def scrape(self):
		for company in self.company_array:
			link = self.base_link+company.symbol+self.end_link
			table_contents = []
			count = 0
			while len(table_contents) == 0:
				finance_site = requests.get(link)
				soup = bs4.BeautifulSoup(finance_site.text)
				table_contents = [td.get_text() for td in soup.select('td.yfnc_tabledata1')]
				count += 1
				if count > 5:
					break ## incase there are server issues/connection issues, but at least try a couple of times
			formatted_list = []
			count = 1
			for value in table_contents:
				if value == "N/A":
					formatted_list.append(0)
				else:
					formatted_list.append(value)

			Stocks.objects.create(company=company,
				market_cap=formatted_list[0],
				enterprise_value=formatted_list[1],
				trailing_pe=formatted_list[2],
				PEG=formatted_list[3],
				price_sales=formatted_list[4],
				price_book=formatted_list[5],
				EV_revenue=formatted_list[6],
				EV_EBITDA=formatted_list[7],
				profit_margin=formatted_list[8],
				operating_margin=formatted_list[11],
				return_on_assets=formatted_list[12],
				return_on_equity=formatted_list[13],
				revenue=formatted_list[14],
				revenue_per_share=formatted_list[15],
				qrtly_revenue_growth=formatted_list[16],
				gross_profit=formatted_list[17],
				EBITDA=formatted_list[18],
				net_income=formatted_list[19],
				diluted_eps=formatted_list[20],
				qrtly_earnings_growth=formatted_list[21],
				total_cash=formatted_list[22],
				total_cash_per_share=formatted_list[23],
				total_debt=formatted_list[24],
				total_debt_equity=formatted_list[25],
				current_ratio=formatted_list[26],
				bv_per_share=formatted_list[27],
				operating_cash_flow=formatted_list[28],
				levered_free_cash_flow=formatted_list[29])
			
			print("success!",company.name)
		return None


Finance_API().scrape()


## Populate DB with companies of Interest ##

list_of_companies = {'Int Business Machines':'IBM','Hewlett-Packard Corp':'HPQ','Xerox':'XRX','Computer Sciences Corp': 'CSC','Unisys Corp':'UIS','CA Technologies':'CA','Oracle':'ORCL','Symantec Corp':'SYMC','Microsoft':'MSFT','Cognizant Technology Corp':'CTSH','Amdocs Limited':'DOX','Compuware Inc':'CPWR','Citrix Corp':'CTXS','Apple Inc':'AAPL','Google':'GOOG'}

def populate_company_list(dict):
	for key in dict:
		Companies.objects.create(name=key,symbol=dict[key])
	print('Populated')
	return None

# run once #
# populate_company_list(list_of_companies)
