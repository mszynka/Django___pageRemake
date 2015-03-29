# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_cms', '0009_auto_20150324_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='posted',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
