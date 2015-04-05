# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('website', models.URLField(blank=True)),
                ('text', models.TextField()),
                ('parent', models.ForeignKey(blank=True, to='blog.Comment')),
                ('post', models.ForeignKey(blank=True, to='blog.Post')),
                ('replies', models.ManyToManyField(blank=True, related_name='Replies', to='blog.Comment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
