# Generated by Django 5.1.3 on 2024-11-22 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_category_rename_phe_number_customer_phone_field_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Products",
            new_name="Product",
        ),
    ]
