# Generated by Django 2.2.6 on 2020-04-27 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20200424_1301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temprature',
            old_name='id',
            new_name='Tid',
        ),
    ]
