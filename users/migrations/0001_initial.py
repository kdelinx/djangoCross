# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64, blank=True, verbose_name='Имя')),
                ('first_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('third_name', models.CharField(max_length=255, verbose_name='Отчество')),
                ('avatar', imagekit.models.fields.ProcessedImageField(upload_to=users.models.get_user_avatar, blank=True, null=True)),
                ('email', models.EmailField(max_length=150, verbose_name='E-mail', unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('number', models.IntegerField(default=0, blank=True, null=True, verbose_name='Уникальный код')),
                ('groups', models.ManyToManyField(blank=True, related_name='user_set', verbose_name='groups', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='user_set', verbose_name='user permissions', related_query_name='user', help_text='Specific permissions for this user.', to='auth.Permission')),
            ],
            options={
                'verbose_name_plural': 'пользователи',
                'verbose_name': 'Пользователь',
            },
        ),
    ]
