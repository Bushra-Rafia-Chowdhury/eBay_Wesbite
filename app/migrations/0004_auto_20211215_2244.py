# Generated by Django 2.2 on 2021-12-15 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211215_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='end_date_time',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='min_bid_price',
            field=models.IntegerField(max_length=10),
        ),
    ]
