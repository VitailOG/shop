# Generated by Django 3.2 on 2021-05-25 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0031_auto_20210525_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sold_out',
        ),
    ]
