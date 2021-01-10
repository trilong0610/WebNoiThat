# Generated by Django 3.1.4 on 2021-01-10 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_sizeproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='amount_sell',
        ),
        migrations.AddField(
            model_name='sizeproduct',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sizeproduct',
            name='amount_sell',
            field=models.IntegerField(default=0),
        ),
    ]
