# Generated by Django 5.0.6 on 2024-07-22 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_payment_order_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_table',
            name='no_of_items',
            field=models.IntegerField(),
        ),
    ]
