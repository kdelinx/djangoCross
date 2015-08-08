# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150730_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(verbose_name='E-mail', max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=64, unique=True, verbose_name='Логин'),
        ),
    ]
