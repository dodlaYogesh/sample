# Generated by Django 4.2.6 on 2023-11-03 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_list_address'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='olist',
            name='view',
            field=models.OneToOneField(default=10, on_delete=django.db.models.deletion.CASCADE, to='products.list'),
        ),
    ]
