# Generated by Django 3.2.2 on 2021-05-18 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0043_alter_address_address_line_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='firmware',
            name='friendly_name',
            field=models.CharField(default='May 2021 v1.2 Final release', help_text='Give it a friendly name e.g. May-2021 1.2 release', max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firmware',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
