# Generated by Django 2.0.3 on 2018-03-31 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0004_auto_20180331_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loggeddevicedata',
            name='value',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='loggedroomdata',
            name='lux_value',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='loggedroomdata',
            name='temp_value',
            field=models.FloatField(default=0),
        ),
    ]