from django.db import models

# Create your models here.

class Companies(models.Model):
	name = models.CharField(max_length=30)
	symbol = models.CharField(max_length=10)

class Stocks(models.Model):
	company = models.ForeignKey(Companies)
	scraped_at = models.DateTimeField(auto_now_add=True)
	market_cap  = models.CharField(max_length=25)
	enterprise_value = models.CharField(max_length=25)
	trailing_pe = models.CharField(max_length=25)
	PEG = models.CharField(max_length=25)
	price_sales = models.CharField(max_length=25)
	price_book = models.CharField(max_length=25)
	EV_revenue = models.CharField(max_length=25)
	EV_EBITDA = models.CharField(max_length=25)
	profit_margin = models.CharField(max_length=25)
	operating_margin = models.CharField(max_length=25)
	return_on_assets = models.CharField(max_length=25)
	return_on_equity = models.CharField(max_length=25)
	revenue = models.CharField(max_length=25)
	revenue_per_share = models.CharField(max_length=25)
	qrtly_revenue_growth = models.CharField(max_length=25)
	gross_profit = models.CharField(max_length=25)
	EBITDA = models.CharField(max_length=25)
	net_income = models.CharField(max_length=25)
	diluted_eps = models.CharField(max_length=25)
	qrtly_earnings_growth = models.CharField(max_length=25)
	total_cash = models.CharField(max_length=25)
	total_cash_per_share = models.CharField(max_length=25)
	total_debt = models.CharField(max_length=25)
	total_debt_equity = models.CharField(max_length=25)
	current_ratio = models.CharField(max_length=25)
	bv_per_share = models.CharField(max_length=25)
	operating_cash_flow = models.CharField(max_length=25)
	levered_free_cash_flow = models.CharField(max_length=25)



