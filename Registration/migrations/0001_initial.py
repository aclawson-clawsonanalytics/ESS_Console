# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_name', models.CharField(max_length=100)),
                ('manager_first', models.CharField(max_length=200)),
                ('manager_last', models.CharField(max_length=200)),
                ('manager_email', models.CharField(max_length=200)),
                ('manager_phone', models.CharField(max_length=10)),
            ],
        ),
    ]
