# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20150404_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='parent',
            field=models.ForeignKey(to='blog.Comment', blank=True),
            preserve_default=True,
        ),
    ]
