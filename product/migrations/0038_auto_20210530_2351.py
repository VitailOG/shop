# Generated by Django 3.2 on 2021-05-30 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0037_auto_20210530_2349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name_ua',
            new_name='name_ru',
        ),
        migrations.RenameField(
            model_name='spec',
            old_name='key_ua',
            new_name='key_ru',
        ),
        migrations.RenameField(
            model_name='spec',
            old_name='value_ua',
            new_name='value_ru',
        ),
    ]
