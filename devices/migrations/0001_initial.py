# Generated by Django 2.0.3 on 2018-03-27 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('nickname', models.CharField(max_length=128)),
                ('usage_number', models.IntegerField()),
                ('wattage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Room'),
        ),
    ]