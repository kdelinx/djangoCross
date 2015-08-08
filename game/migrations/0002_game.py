# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('x1', models.SmallIntegerField(verbose_name='row 1 cell 1')),
                ('x2', models.SmallIntegerField(verbose_name='row 1 cell 2')),
                ('x3', models.SmallIntegerField(verbose_name='row 1 cell 3')),
                ('x4', models.SmallIntegerField(verbose_name='row 2 cell 1')),
                ('x5', models.SmallIntegerField(verbose_name='row 2 cell 2')),
                ('x6', models.SmallIntegerField(verbose_name='row 2 cell 3')),
                ('x7', models.SmallIntegerField(verbose_name='row 3 cell 1')),
                ('x8', models.SmallIntegerField(verbose_name='row 3 cell 2')),
                ('x9', models.SmallIntegerField(verbose_name='row 3 cell 3')),
                ('first_player', models.ForeignKey(verbose_name='First user', to=settings.AUTH_USER_MODEL, related_name='first_user_game')),
                ('second_player', models.ForeignKey(verbose_name='Second user', to=settings.AUTH_USER_MODEL, related_name='second_user_game')),
            ],
            options={
                'verbose_name': 'Игровой процесс',
                'verbose_name_plural': 'Игровой процесс',
            },
        ),
    ]
