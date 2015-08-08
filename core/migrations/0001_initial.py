# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('page', models.CharField(max_length=64, verbose_name='Название страницы(en)')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('body', models.TextField(verbose_name='Текст страницы')),
            ],
            options={
                'verbose_name_plural': 'статьи',
                'verbose_name': 'Статьи',
            },
        ),
    ]
