# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-08 06:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160908_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='comtent',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]