# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_cms', '0004_auto_20150322_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='view',
            old_name='disabled',
            new_name='enabled',
        ),
    ]
