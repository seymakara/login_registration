# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-18 08:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='pw_hash',
            new_name='password',
        ),
    ]
