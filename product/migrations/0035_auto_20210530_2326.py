# Generated by Django 3.2 on 2021-05-30 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0034_auto_20210530_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name_ua',
            new_name='name_uk',
        ),
        migrations.RenameField(
            model_name='spec',
            old_name='key_ua',
            new_name='key_uk',
        ),
        migrations.RenameField(
            model_name='spec',
            old_name='value_ua',
            new_name='value_uk',
        ),
    ]
