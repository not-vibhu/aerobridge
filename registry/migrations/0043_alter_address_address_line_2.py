# Generated by Django 3.2.1 on 2021-05-12 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0042_alter_address_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]
