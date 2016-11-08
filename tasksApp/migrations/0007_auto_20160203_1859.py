# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasksApp', '0006_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='solution',
        ),
        migrations.RemoveField(
            model_name='check',
            name='badComment',
        ),
        migrations.RemoveField(
            model_name='check',
            name='goodComment',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
