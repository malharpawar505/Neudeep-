# Generated by Django 4.0.2 on 2022-04-17 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.IntegerField(primary_key=b'I01\n', serialize=False)),
                ('brand', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('flavour', models.CharField(max_length=100)),
                ('weight', models.IntegerField()),
                ('no_of_cartoons', models.IntegerField()),
                ('price_per_cartoon', models.IntegerField()),
                ('Distributor_name', models.CharField(max_length=100)),
                ('area_name', models.CharField(max_length=100)),
                ('inventory_with', models.CharField(max_length=100)),
                ('sold_to_type', models.CharField(max_length=100)),
                ('Product_mrp', models.BigIntegerField()),
                ('upc_bar_code', models.CharField(max_length=100)),
                ('bar_count', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sales',
            fields=[
                ('id', models.IntegerField(primary_key=b'I01\n', serialize=False)),
                ('brand', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('flavour', models.CharField(max_length=100)),
                ('weight', models.IntegerField()),
                ('no_of_cartoons', models.IntegerField()),
                ('price_per_cartoon', models.IntegerField()),
                ('Distributor_name', models.CharField(max_length=100)),
                ('area_name', models.CharField(max_length=100)),
                ('sales_person', models.CharField(max_length=100)),
                ('total_buisness', models.BigIntegerField()),
                ('inventory_with', models.CharField(max_length=100)),
                ('sold_to_type', models.CharField(max_length=100)),
                ('Product_mrp', models.BigIntegerField()),
                ('upc_bar_code', models.CharField(max_length=100)),
                ('bar_count', models.CharField(max_length=100)),
                ('ware_house_name', models.CharField(max_length=100)),
                ('sold_to_id', models.IntegerField()),
            ],
        ),
    ]
