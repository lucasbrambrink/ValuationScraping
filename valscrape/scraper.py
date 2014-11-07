import requests
import datetime
import time
import random
import bs4
import json
import re
# from valscrape.models import Stock


class Finance_API:
	def __init__(self):
		self.base_link = 'http://finance.yahoo.com/q/ks?s='
		self.end_link = '+Key+Statistics'
		self.company_array = ['GOOG'] # ,'APPL', ...]

	def scrape(self):
		for stock in self.company_array:
			link = self.base_link+stock+self.end_link
			finance_site = requests.get(link)
			soup = bs4.BeautifulSoup(finance_site.text)
			market_cap = [td.get_text() for td in soup.select('td.yfnc_tabledata1')]

			print(market_cap)
			return None


Finance_API().scrape()



