# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000, default='')),
                ('goodComment', models.CharField(max_length=200, default='Good!')),
                ('badComment', models.CharField(max_length=200, default='Bad!')),
            ],
        ),
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('checks', models.ManyToManyField(to='tasksApp.Check')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('comment', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('creation_date', models.DateTimeField(null=True)),
                ('student_email', models.EmailField(max_length=70, null=True, blank=True)),
                ('content', models.CharField(max_length=3000, default='')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('value', models.BooleanField(default=False)),
                ('chk', models.ForeignKey(to='tasksApp.Check')),
                ('solution', models.ForeignKey(to='tasksApp.Solution')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1200)),
                ('feedb_templ_1', models.CharField(max_length=200, default='')),
                ('feedb_templ_2', models.CharField(max_length=200, default='')),
                ('checkList', models.ForeignKey(to='tasksApp.CheckList', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='solution',
            name='task',
            field=models.ForeignKey(to='tasksApp.Task'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='solution',
            field=models.ForeignKey(to='tasksApp.Solution'),
        ),
    ]
