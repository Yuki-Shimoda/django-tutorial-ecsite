# Generated by Django 2.2.24 on 2021-07-07 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='quantitiy',
            new_name='quantity',
        ),
    ]
