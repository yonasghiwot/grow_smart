# Generated by Django 4.0.6 on 2024-09-01 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TimeStamp', models.DateTimeField()),
                ('Temprature', models.CharField(max_length=5)),
                ('Humidity', models.CharField(max_length=5)),
                ('PH', models.CharField(max_length=5)),
                ('EC', models.CharField(max_length=4)),
            ],
        ),
    ]
