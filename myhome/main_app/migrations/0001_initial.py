# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-04 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('telephone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('qq', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]
