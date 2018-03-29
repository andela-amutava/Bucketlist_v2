# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-13 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_bucketlistitems'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bucketlist',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='bucketlistitems',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='bucketlistitems',
            name='bucketlist_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bucketlist', to='api.Bucketlist'),
        ),
    ]