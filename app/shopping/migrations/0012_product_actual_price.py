# Generated by Django 3.1.7 on 2021-04-02 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0011_remove_product_current_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='actual_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
