# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160129_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patronage',
            name='url',
            field=models.CharField(default='', blank=True, max_length=200),
        ),
    ]
