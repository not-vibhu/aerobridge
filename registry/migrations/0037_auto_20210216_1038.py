# Generated by Django 3.1.6 on 2021-02-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0036_auto_20210215_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='dot_permission_document',
            field=models.URLField(default='https://raw.githubusercontent.com/openskies-sh/aerobridge/master/sample-data/Aerobridge-placeholder-document.pdf', help_text='Link to Purchased RPA has ETA from WPC Wing, DoT for operating in the de-licensed frequency band(s). Such approval shall be valid for a particular make and model'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='operataions_manual_document',
            field=models.URLField(default='https://raw.githubusercontent.com/openskies-sh/aerobridge/master/sample-data/Aerobridge-placeholder-document.pdf', help_text='Link to Operation Manual Document'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='cin_document',
            field=models.URLField(default='https://raw.githubusercontent.com/openskies-sh/aerobridge/master/sample-data/Aerobridge-placeholder-document.pdf', help_text='Link to certificate of Incorporation issued by ROC, MCA'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='eta_document',
            field=models.URLField(default='https://raw.githubusercontent.com/openskies-sh/aerobridge/master/sample-data/Aerobridge-placeholder-document.pdf', help_text='Link to Equipment Type Approval (ETA) from WPC Wing'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='gst_document',
            field=models.URLField(default='https://raw.githubusercontent.com/openskies-sh/aerobridge/master/sample-data/Aerobridge-placeholder-document.pdf', help_text='Link to GST certification document'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='pan_card_document',
            field=models.URLField(default='https://raw.githubusercontent.com/openskies-sh/aerobridge/master/sample-data/Aerobridge-placeholder-document.pdf', help_text='URL of Manufacturers PAN Card scan'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='security_clearance_document',
            field=models.URLField(default='https://raw.githubusercontent.com/openskies-sh/aerobridge/master/sample-data/Aerobridge-placeholder-document.pdf', help_text='Link to Security Clearance from Ministry of Home Affairs'),
        ),
    ]
