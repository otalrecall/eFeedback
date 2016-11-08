# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasksApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='creation_date',
            field=models.DateTimeField(),
        ),
    ]
