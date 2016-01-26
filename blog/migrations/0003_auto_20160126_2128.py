# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
