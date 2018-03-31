# Generated by Django 2.0.3 on 2018-03-31 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_auto_20180330_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loggedroomdata',
            old_name='value',
            new_name='lux_value',
        ),
        migrations.AddField(
            model_name='loggedroomdata',
            name='temp_value',
            field=models.IntegerField(default=0),
        ),
    ]
