# Generated by Django 3.2 on 2021-04-28 18:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0023_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 28, 18, 37, 28, 163684, tzinfo=utc), verbose_name='Дата на виконання'),
        ),
    ]
