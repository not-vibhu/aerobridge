# Generated by Django 3.1.3 on 2020-11-30 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcs_operations', '0005_auto_20201129_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightplan',
            name='name',
            field=models.CharField(default='Flight Plan yrfbbz', max_length=20),
        ),
    ]
