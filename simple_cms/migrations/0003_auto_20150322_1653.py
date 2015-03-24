# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_cms', '0002_auto_20150322_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='link',
            field=models.CharField(max_length=80),
            preserve_default=True,
        ),
    ]
