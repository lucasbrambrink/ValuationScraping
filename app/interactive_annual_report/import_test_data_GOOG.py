import sys, os
sys.path.append('../../app')
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
import django
django.setup()
from interactive_annual_report import models
from datetime import datetime

try:
    internet = models.Industry.objects.create(name='Internet Information Providers')
except:
    internet = models.Industry.objects.get(name='Internet Information Providers')
try:
    tech = models.Sector.objects.create(name='Technology')
except:
    tech = models.Sector.objects.get(name='Technology')

goog = models.Stock(symbol='IBM', name='International Business Machines Corporation', sector=tech, industry=internet)
try:
    goog.save()
except:
    goog = models.Stock.objects.get(symbol='IBM')

annual_report_data = {
    'year': datetime.strptime('Dec 31, 2013', '%b %d, %Y'),
    'tr': 99751000,
    'gt': 48505000,
    'ebit': 19926000,
    'ie': 402000,
    'ibt': 19524000,
    'ite': 3041000,
    'ni': 16483000,
    'cce': 10716000,
    'sti': 350000,
    'inventory': 2310000,
    'tca': 51350000,
    'ppe': 13821000,
    'ta': 126223000,
    'tcl': 6862000,
    'ltd': 32856000,
    'mi': 137000,
    'td': 39718000,
    'tl': 103431000,
    'ps': 0,
    'tse': 22792000,
    'tcso': 1054390,
    'sp': 187.57,
    'dp': -4058000,

    'stock': goog
}

try:
    goog_report = goog.annualreport_set.create(**annual_report_data)
except:
    goog_report = goog.annualreport_set.get(year='2013-12-31')

key_statics_data = {
            'bvps': annual_report_data['tse'] / annual_report_data['tcso'],
            'dpr': 0,
            'dy': 0,
            'per': 0,
            'pegr': 0,
            'psr': 0,
            'cashr': 0,
            'currentr': 0,
            'qr': 0,
            'pm': 0,
            'etr': 0,
            'roa': 0,
            'roce': 0,
            'roe': 0,
            'dar': 0,
            'der': 0,
            'icr': 0,
            'fatr': 0,
            'scfr': 0,
            'ev': 0
        }

report_key_statics = models.KeyStatics(annual_report=goog_report, **key_statics_data)
report_key_statics.save()