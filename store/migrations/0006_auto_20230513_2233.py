# Generated by Django 3.1 on 2023-05-13 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_seller_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
