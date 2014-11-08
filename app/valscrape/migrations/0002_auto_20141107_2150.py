# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valscrape', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='EBITDA',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='enterprise_value',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='levered_free_cash_flow',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='market_cap',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='net_income',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='operating_cash_flow',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='operating_margin',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='profit_margin',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='qrtly_earnings_growth',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='qrtly_revenue_growth',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='return_on_assets',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='return_on_equity',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='revenue',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='total_cash',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='total_debt',
            field=models.CharField(max_length=25),
        ),
    ]
