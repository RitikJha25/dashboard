# Generated by Django 2.2.6 on 2020-04-24 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20200423_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temprature',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
