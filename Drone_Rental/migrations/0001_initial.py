# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('billing_days', models.IntegerField()),
                ('status', models.CharField(choices=[('iq', 'inquiry'), ('bk', 'booked'), ('cn', 'cancelled'), ('bl', 'billed'), ('pd', 'payed')], default='bk', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('street', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('drone_model', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('camera', models.CharField(max_length=200)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='customer',
            field=models.ForeignKey(to='Drone_Rental.Customer'),
        ),
        migrations.AddField(
            model_name='case',
            name='drone',
            field=models.ForeignKey(to='Drone_Rental.Drone'),
        ),
    ]
