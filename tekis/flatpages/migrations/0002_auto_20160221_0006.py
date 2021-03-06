# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-20 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='flatpage_type',
            field=models.IntegerField(choices=[(0, 'Page'), (1, 'Direct Link')], default=0),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='menu_category',
            field=models.IntegerField(choices=[(1, b'Association'), (2, b'Activities'), (0, b'(Top level)')], default=0),
        ),
        migrations.AlterField(
            model_name='localflatpage',
            name='content_markup',
            field=models.CharField(choices=[(b'textile', b'Textile'), (b'none', b'None (no processing)'), (b'linebreaks', b'Linebreaks')], default=b'textile', max_length=20),
        ),
        migrations.AlterField(
            model_name='localflatpage',
            name='url',
            field=models.CharField(blank=True, db_index=True, max_length=100),
        ),
    ]
