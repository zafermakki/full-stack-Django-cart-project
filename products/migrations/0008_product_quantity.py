# Generated by Django 4.2 on 2024-07-28 11:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0007_remove_product_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="quantity",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
