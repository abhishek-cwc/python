# Generated by Django 4.2.21 on 2025-05-23 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_remove_mproduct_category_mproduct_category_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mcategory',
            name='price',
        ),
        migrations.RemoveField(
            model_name='mcategory',
            name='qty',
        ),
        migrations.RemoveField(
            model_name='mcategory',
            name='sku',
        ),
    ]
