# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisis', '0014_auto_20170409_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='category',
            field=models.IntegerField(choices=[(0, 'Fire'), (1, 'Traffic Accient'), (2, 'Terrorist Attack'), (3, 'Gas leak')]),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='userType',
            field=models.IntegerField(choices=[(0, 'Call Operator'), (1, 'Civil Defense'), (2, 'Police'), (3, 'Singapore power')], null=True),
        ),
    ]