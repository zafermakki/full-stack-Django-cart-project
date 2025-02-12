# Generated by Django 4.2 on 2024-09-17 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0012_delete_cartitem"),
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartproduct",
            name="cart",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="cart.cart"
            ),
        ),
        migrations.AlterField(
            model_name="cartproduct",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="products.product"
            ),
        ),
        migrations.AlterModelTable(
            name="cart",
            table="cart",
        ),
    ]
