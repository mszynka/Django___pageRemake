# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_cms', '0007_auto_20150324_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='view',
            field=models.ForeignKey(default=1, to='simple_cms.View'),
            preserve_default=True,
        ),
    ]
