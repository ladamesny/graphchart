# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('temperature', models.IntegerField(default=0)),
                ('reading_time', models.DateTimeField(verbose_name='time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
