# Generated by Django 2.2.24 on 2021-07-07 03:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210707_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 7, 7, 3, 6, 11, 571037, tzinfo=utc)),
        ),
    ]
