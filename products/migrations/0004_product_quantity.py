# Generated by Django 4.2 on 2024-07-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_product_video_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="quantity",
            field=models.IntegerField(default=0),
        ),
    ]
