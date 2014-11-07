import requests
import datetime
import time
import random
import bs4
import json
import re
from valscrape.models import Stocks,Companies

## Scrape Yahoo Finance for Stock Information ##

class Finance_API:
	def __init__(self):
		self.base_link = 'http://finance.yahoo.com/q/ks?s='
		self.end_link = '+Key+Statistics'
		self.company_array = Companies.objects.all()#['GOOG'] # ,'APPL', ...]

	def scrape(self):
		for company in self.company_array:
			link = self.base_link+stock+self.end_link
			table_contents = []
			count = 0
			while len(table_contents) == 0:
				finance_site = requests.get(link)
				soup = bs4.BeautifulSoup(finance_site.text)
				table_contents = [td.get_text() for td in soup.select('td.yfnc_tabledata1')]
				count += 1
				if count > 10:
					break ## incase there are server issues/connection issues, but at least try a couple of times
			Stocks.objects.create(company=company,
				market_cap=table_contents[0],
				enterprise_value=table_contents[1],
				trailing_pe=table_contents[2],
				PEG=table_contents[3],
				price_sales=table_contents[4],
				price_book=table_contents[5],
				EV_revenue=table_contents[6],
				EV_EBITDA=table_contents[7],
				profit_margin=table_contents[8],
				operating_margin=table_contents[11],
				return_on_assets=table_contents[12],
				return_on_equity=table_contents[13],
				revenue=table_contents[14],
				revenue_per_share=table_contents[15],
				qrtly_revenue_growth=table_contents[16],
				gross_profit=table_contents[17],
				EBITDA=table_contents[18],
				net_income=table_contents[19],
				diluted_eps=table_contents[20],
				qrtly_earnings_growth=table_contents[21],
				total_cash=table_contents[22],
				total_cash_per_share=table_contents[23],
				total_debt=table_contents[24],
				total_debt_equity=table_contents[25],
				current_ratio=table_contents[26],
				bv_per_share=table_contents[27],
				operating_cash_flow=table_contents[28],
				levered_free_cash_flow=table_contents[29])
			return table_contents


print(Finance_API().scrape())


## Populate DB with companies of Interest ##

list_of_companies = {'International Business Machines':'IBM','Hewlett-Packard Corp':'HPQ','Xerox':'XRX','Computer Sciences Corp': 'CSC','Unisys Corp':'UIS','CA Technologies':'CA','Oracle':'ORCL','Symantec Corp':'SYMC','Microsoft':'MSFT','Cognizant Technology Corp':'CTSH','Amdocs Limited':'DOX','Compuware Inc':'CPWR','Citrix Corp':'CTXS','Apple Inc':'AAPL','Google':'GOOG'}

def populate_company_list(dict):
	for key in dict:
		Company.objects.create(name=key,symbol=dict[key])
	print('Populated')
	return None

