# Generated by Django 4.2 on 2024-07-01 18:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_product_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="video_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]