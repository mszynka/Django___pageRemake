# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_tag_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(max_length=10, default='gray', choices=[('red', 'red'), ('aqua', 'aqua'), ('blue', 'blue'), ('purple', 'purple'), ('lime', 'lime'), ('green', 'green'), ('yellow', 'yellow'), ('orange', 'orange'), ('gray', 'gray')]),
            preserve_default=True,
        ),
    ]
