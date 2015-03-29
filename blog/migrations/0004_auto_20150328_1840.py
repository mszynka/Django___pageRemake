# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150328_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': ' > Categories'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': '  Posts'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': ' > Tags'},
        ),
    ]
