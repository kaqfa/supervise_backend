# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-27 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0005_auto_20161227_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='file',
            field=models.ManyToManyField(blank=True, to='progress.MediaFile'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='type',
            field=models.CharField(choices=[('w', 'pengerjaan'), ('e', 'penjelasan'), ('q', 'pertanyaan')], default='w', max_length=1),
        ),
    ]
