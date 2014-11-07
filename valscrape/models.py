from django.db import models

# Create your models here.

class Company(models.Model):
	name = models.CharField(max_length=30)
	symbol = models.CharField(max_length=10)

class Stock(models.Model):
	company = models.ForeignKey(Company)
	market_cap  = models.DecimalField(max_digits=8, decimal_places=5)
	enterprise_value = models.DecimalField(max_digits=8, decimal_places=5)
	trailing_pe = models.DecimalField(max_digits=8, decimal_places=5)
	PEG = models.DecimalField(max_digits=8, decimal_places=5)
	price_sales = models.DecimalField(max_digits=8, decimal_places=5)
	price_book = models.DecimalField(max_digits=8, decimal_places=5)
	EV_revenue = models.DecimalField(max_digits=8, decimal_places=5)
	EV_EBITDA = models.DecimalField(max_digits=8, decimal_places=5)
	profit_margin = models.DecimalField(max_digits=8, decimal_places=5)
	operating_margin = models.DecimalField(max_digits=8, decimal_places=5)
	return_on_assets = models.DecimalField(max_digits=8, decimal_places=5)
	return_on_equity = models.DecimalField(max_digits=8, decimal_places=5)
	revenue = models.DecimalField(max_digits=8, decimal_places=5)
	revenue_per_share = models.DecimalField(max_digits=8, decimal_places=5)
	qrtly_revenue_growth = models.DecimalField(max_digits=8, decimal_places=5)
	gross_profit = models.DecimalField(max_digits=8, decimal_places=5)
	EBITDA = models.DecimalField(max_digits=8, decimal_places=5)
	net_income = models.DecimalField(max_digits=8, decimal_places=5)
	diluted_eps = models.DecimalField(max_digits=8, decimal_places=5)
	qrtly_earnings_growth = models.DecimalField(max_digits=8, decimal_places=5)
	total_cash = models.DecimalField(max_digits=8, decimal_places=5)
	total_cash_per_share = models.DecimalField(max_digits=8, decimal_places=5)
	total_debt = models.DecimalField(max_digits=8, decimal_places=5)
	total_debt_equity = models.DecimalField(max_digits=8, decimal_places=5)
	current_ratio = models.DecimalField(max_digits=8, decimal_places=5)
	bv_per_share = models.DecimalField(max_digits=8, decimal_places=5)
	operating_cash_flow = models.DecimalField(max_digits=8, decimal_places=5)
	levered_free_cash_flow = models.DecimalField(max_digits=8, decimal_places=5)
	created_at = models.DateTimeField(auto_now_add=True)
