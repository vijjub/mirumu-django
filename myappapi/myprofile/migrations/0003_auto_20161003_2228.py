# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-03 22:28
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0002_auto_20160928_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='laundry',
        ),
        migrations.AddField(
            model_name='apartment',
            name='age',
            field=models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(17), django.core.validators.MaxValueValidator(130)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apartment',
            name='airConditioner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apartment',
            name='closet',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apartment',
            name='deposit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apartment',
            name='drugs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apartment',
            name='dryer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apartment',
            name='furnished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apartment',
            name='gender',
            field=models.CharField(default='M', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apartment',
            name='guests',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apartment',
            name='hasPet',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apartment',
            name='heater',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apartment',
            name='kitchen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apartment',
            name='lateNights',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apartment',
            name='music',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apartment',
            name='washer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='pets',
            field=models.BooleanField(default=False),
        ),
    ]
