# Generated by Django 4.0.2 on 2022-04-17 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutriapi', '0002_order_date_sales_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Product_mrp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Product_mrp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sales',
            name='total_buisness',
            field=models.IntegerField(),
        ),
    ]
