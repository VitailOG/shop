# Generated by Django 3.2 on 2021-04-24 14:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 24, 14, 46, 48, 210998, tzinfo=utc), verbose_name='Дата на виконання'),
        ),
    ]
