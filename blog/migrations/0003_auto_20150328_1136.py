# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150328_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('attribute', models.CharField(max_length=100, unique=True)),
                ('value', models.CharField(default='0', max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Settings',
                'verbose_name': 'Attribute',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
