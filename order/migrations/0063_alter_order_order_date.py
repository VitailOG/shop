# Generated by Django 3.2 on 2021-06-09 15:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0062_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 9, 15, 25, 8, 639359, tzinfo=utc), verbose_name='Дата на виконання'),
        ),
    ]
