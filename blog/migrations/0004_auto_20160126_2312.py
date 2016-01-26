# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160126_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patronage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='partners/')),
                ('type', models.SmallIntegerField(choices=[(0, 'Patron'), (1, 'Partner'), (2, 'Sponsor')])),
            ],
        ),
        migrations.AlterField(
            model_name='bio',
            name='img',
            field=models.ImageField(upload_to='bios/'),
        ),
    ]
