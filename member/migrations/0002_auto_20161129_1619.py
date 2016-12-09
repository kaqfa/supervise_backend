# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 09:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='supervisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member'),
        ),
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]