# Generated by Django 3.2 on 2021-05-30 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0033_auto_20210530_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title_ua',
        ),
    ]
