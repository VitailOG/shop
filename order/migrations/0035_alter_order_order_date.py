# Generated by Django 3.2 on 2021-05-21 20:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0034_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 21, 20, 41, 33, 19311, tzinfo=utc), verbose_name='Дата на виконання'),
        ),
    ]
