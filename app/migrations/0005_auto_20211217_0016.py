# Generated by Django 2.2 on 2021-12-16 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211215_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='min_bid_price',
            field=models.CharField(max_length=10),
        ),
    ]