# Generated by Django 3.2 on 2021-06-16 12:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0067_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 16, 12, 13, 25, 475942, tzinfo=utc), verbose_name='Дата на виконання'),
        ),
    ]
