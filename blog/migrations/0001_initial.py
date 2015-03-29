# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(unique=True, max_length=150)),
                ('slug', models.SlugField(unique=True, max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(unique=True, max_length=150)),
                ('slug', models.SlugField(unique=True, max_length=150)),
                ('text', models.TextField()),
                ('date', models.DateField(db_index=True, auto_now_add=True)),
                ('category', models.ForeignKey(to='blog.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
