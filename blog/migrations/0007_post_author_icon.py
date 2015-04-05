# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_icon',
            field=models.ImageField(upload_to='', blank=True),
            preserve_default=True,
        ),
    ]
