# Generated by Django 3.1 on 2023-05-15 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20230515_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryBoy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('vehicle_no', models.CharField(max_length=20)),
                ('license_no', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deliveryboy', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
