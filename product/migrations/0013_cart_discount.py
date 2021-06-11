# Generated by Django 3.2 on 2021-04-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_cart_all_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Сума із знижкою'),
        ),
    ]
