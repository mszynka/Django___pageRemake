# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_cms', '0010_article_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userss',
            name='mail',
            field=models.EmailField(max_length=254),
        ),
    ]
