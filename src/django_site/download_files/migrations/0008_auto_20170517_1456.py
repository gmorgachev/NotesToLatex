# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-17 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download_files', '0007_auto_20170514_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='profilephoto',
            name='file',
            field=models.ImageField(upload_to=b''),
        ),
    ]