from django.db import models


class Sector(models.Model):
    name = models.CharField(max_length=40, default="", unique=True)


class Industry(models.Model):
    name = models.CharField(max_length=40, default="", unique=True)


class Stock(models.Model):
    """
    A class for storing stock profile
    """
    name = models.CharField(max_length=80, default="")
    symbol = models.CharField(max_length=10, blank=False, unique=True)
    sector = models.ForeignKey(Sector)
    industry = models.ForeignKey(Industry)


class AnnualReport(models.Model):
    """
    A class for storing annual report
    """
    year = models.DateField(blank=False)
    # Total Revenue
    tr = models.IntegerField()
    # Gross Profit
    gt = models.IntegerField()
    # Earning Before Interest and Taxes
    ebit = models.IntegerField()
    # Interest Expense
    ie = models.IntegerField()
    # Income Before Tax
    ibt = models.IntegerField()
    # Income Tax Expense
    ite = models.IntegerField()
    # Net Income
    ni = models.IntegerField()
    # Cash And Cash Equivalents
    cce = models.IntegerField()
    #Short Term Investments
    sti = models.IntegerField()
    # Inventory
    inventory = models.IntegerField()
    # Total Current Asset
    tca = models.IntegerField()
    # Property Plant and Equipment
    ppe = models.IntegerField()
    # Total Assets
    ta = models.IntegerField()
    # Total Current Liabilities
    tcl = models.IntegerField()
    # Long Term Debt
    ltd = models.IntegerField()
    # Minority Interest
    mi = models.IntegerField()
    # Total Debt
    td = models.IntegerField()
    # Total Liabilities
    tl = models.IntegerField()
    # Preferred Stock
    ps = models.IntegerField()
    # Total Stockholder Equity
    tse = models.IntegerField()
    # Total common Shares Outstanding
    tcso = models.IntegerField()
    # Stock price
    sp = models.DecimalField(max_digits=8, decimal_places=4)
    # Dividends Paid
    dp = models.IntegerField()

    stock = models.ForeignKey(Stock)


class KeyStatics(models.Model):
    """
    A class for storing key statics analysis for an annual report
    """
    # Book Value Per Share
    bvps = models.DecimalField(max_digits=8, decimal_places=4)
    # Dividend Payout Ratio
    dpr = models.DecimalField(max_digits=8, decimal_places=4)
    # Dividend Yield
    dy =  models.DecimalField(max_digits=8, decimal_places=4)
    # Price to Earnings Ratio
    per = models.DecimalField(max_digits=8, decimal_places=4)
    # PEG Ratio
    pegr = models.DecimalField(max_digits=8, decimal_places=4)
    # Price to Sales Ratio
    psr = models.DecimalField(max_digits=8, decimal_places=4)

    # Cash ratio
    cashr = models.DecimalField(max_digits=8, decimal_places=4)
    # Current Ratio
    currentr = models.DecimalField(max_digits=8, decimal_places=4)
    # Quick Ratio
    qr = models.DecimalField(max_digits=8, decimal_places=4)

    # Profit Margin
    pm = models.DecimalField(max_digits=8, decimal_places=4)
    # Effective Tax Rate
    etr = models.DecimalField(max_digits=8, decimal_places=4)
    # Return on Assets
    roa = models.DecimalField(max_digits=8, decimal_places=4)
    # Return on Captial Employed
    roce = models.DecimalField(max_digits=8, decimal_places=4)
    # Return on Equity
    roe = models.DecimalField(max_digits=8, decimal_places=4)

    # Debt to Asset Ratio
    dar = models.DecimalField(max_digits=8, decimal_places=4)
    # Debt to Equity Ratio
    der = models.DecimalField(max_digits=8, decimal_places=4)
    # Interest Coverage Ratio
    icr = models.DecimalField(max_digits=8, decimal_places=4)

    # Fixed Asset Turnover Ratio
    fatr = models.DecimalField(max_digits=8, decimal_places=4)

    # Sales to Cash Flow Ratio
    scfr = models.DecimalField(max_digits=8, decimal_places=4)

    # Enterprise Value
    ev = models.DecimalField(max_digits=16, decimal_places=4)

    annual_report = models.OneToOneField(AnnualReport, primary_key=True)
