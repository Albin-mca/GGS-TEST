# Generated by Django 3.1 on 2023-05-15 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0006_deliveryboy'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryboy',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
