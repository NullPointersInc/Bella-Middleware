# Generated by Django 2.0.3 on 2018-03-31 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0006_auto_20180331_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loggeddevicedata',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]
