# Generated by Django 4.1.4 on 2024-09-07 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_data_app', '0002_controlparameters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlparameters',
            name='TimeStamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
