# Generated by Django 3.2 on 2021-05-31 11:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0049_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 31, 11, 17, 53, 952974, tzinfo=utc), verbose_name='Дата на виконання'),
        ),
    ]
