# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0016_productimages_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True),
        ),
    ]