# Generated by Django 3.2 on 2021-04-24 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_alter_cart_all_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Сума із знижкою'),
        ),
    ]
