# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_cms', '0005_auto_20150322_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='enabled',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
