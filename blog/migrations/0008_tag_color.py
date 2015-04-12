# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_author_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='color',
            field=models.CharField(default='Black', choices=[('Red', '.red'), ('Aqua', '.aqua'), ('Blue', '.blue'), ('Purple', '.purple'), ('Lime', '.lime'), ('Green', '.green'), ('Yellow', '.yellow'), ('Orange', '.orange'), ('Gray', '.gray'), ('Black', '.black')], max_length=10),
            preserve_default=True,
        ),
    ]
