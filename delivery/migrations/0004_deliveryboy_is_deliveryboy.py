# Generated by Django 3.1 on 2023-05-15 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_deliveryboy'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryboy',
            name='is_deliveryboy',
            field=models.BooleanField(default=True),
        ),
    ]
