# Generated by Django 3.1.4 on 2020-12-22 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0006_auto_20201222_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseproduct',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 22, 18, 10, 31, 725363)),
        ),
    ]
