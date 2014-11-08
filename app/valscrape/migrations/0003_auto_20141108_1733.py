# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valscrape', '0002_auto_20141107_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='EV_EBITDA',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='EV_revenue',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='PEG',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='bv_per_share',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='current_ratio',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='diluted_eps',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='gross_profit',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='price_book',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='price_sales',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='revenue_per_share',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='total_cash_per_share',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='total_debt_equity',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='trailing_pe',
            field=models.CharField(max_length=25),
        ),
    ]
