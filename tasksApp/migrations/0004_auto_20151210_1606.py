# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasksApp', '0003_auto_20151207_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=1000)),
                ('solution', models.ForeignKey(to='tasksApp.Solution')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='check',
            name='task',
        ),
        migrations.RemoveField(
            model_name='check',
            name='value',
        ),
        migrations.AddField(
            model_name='check',
            name='badComment',
            field=models.CharField(default=b'Bad!', max_length=200),
        ),
        migrations.AddField(
            model_name='check',
            name='goodComment',
            field=models.CharField(default=b'Good!', max_length=200),
        ),
        migrations.AddField(
            model_name='state',
            name='chk',
            field=models.ForeignKey(to='tasksApp.Check'),
        ),
        migrations.AddField(
            model_name='state',
            name='solution',
            field=models.ForeignKey(to='tasksApp.Solution'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='checks',
            field=models.ManyToManyField(to='tasksApp.Check'),
        ),
        migrations.AddField(
            model_name='task',
            name='checkList',
            field=models.ForeignKey(to='tasksApp.CheckList', null=True),
        ),
    ]
