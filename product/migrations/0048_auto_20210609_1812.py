# Generated by Django 3.2 on 2021-06-09 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0047_auto_20210608_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AlterField(
            model_name='spec',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
