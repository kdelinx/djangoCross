# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('score', models.SmallIntegerField(verbose_name='Количество балов')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user_score', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name_plural': 'Таблица результатов',
                'verbose_name': 'Таблица результата',
            },
        ),
    ]
