# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2021-11-06 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fat', models.IntegerField()),
                ('stupid', models.IntegerField()),
                ('dumb', models.IntegerField()),
            ],
            options={
                'verbose_name': 'User',
                'db_table': '',
                'managed': True,
                'verbose_name_plural': 'Users',
            },
        ),
    ]