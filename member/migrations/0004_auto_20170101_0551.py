# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-31 22:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20161227_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertise',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.CharField(choices=[('a', 'aktif'), ('b', 'banned'), ('n', 'nonaktif'), ('g', 'lulus')], default='a', max_length=1),
        ),
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
