# Generated by Django 3.1.4 on 2021-01-10 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0020_auto_20210110_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseproduct',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 10, 16, 20, 46, 335109)),
        ),
    ]
