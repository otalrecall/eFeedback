# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasksApp', '0004_auto_20151210_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='feedb_templ_1',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='task',
            name='feedb_templ_2',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
