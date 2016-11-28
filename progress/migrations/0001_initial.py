# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 04:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='1', max_length=1)),
                ('text', models.TextField()),
                ('post_date', models.DateField(auto_now_add=True)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.FileField(upload_to='')),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
        migrations.CreateModel(
            name='StudentTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='1', max_length=1)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('duration', models.SmallIntegerField()),
                ('files', models.ManyToManyField(null=True, to='progress.MediaFile')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('task', models.ManyToManyField(null=True, to='progress.Task')),
            ],
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('abstract', models.TextField(null=True)),
                ('save_date', models.DateField(auto_now_add=True)),
                ('field', models.ManyToManyField(null=True, to='member.Expertise')),
                ('files', models.ManyToManyField(null=True, to='progress.MediaFile')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
        migrations.AddField(
            model_name='studenttask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='progress.Task'),
        ),
        migrations.AddField(
            model_name='comment',
            name='file',
            field=models.ManyToManyField(null=True, to='progress.MediaFile'),
        ),
    ]
