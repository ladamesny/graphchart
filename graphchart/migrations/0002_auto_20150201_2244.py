# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphchart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='reading_time',
            field=models.DateTimeField(verbose_name='time of reading'),
            preserve_default=True,
        ),
    ]
