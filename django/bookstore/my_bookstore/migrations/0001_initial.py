# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-08 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('price', models.FloatField()),
                ('genre', models.CharField(choices=[('H', 'History'), ('C', 'Classic'), ('F', 'Fiction'), ('NF', 'Non-fiction'), ('M', 'Mystery')], max_length=200)),
            ],
        ),
    ]
