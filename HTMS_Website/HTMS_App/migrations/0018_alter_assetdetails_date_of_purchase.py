# Generated by Django 4.1.1 on 2023-02-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("HTMS_App", "0017_alter_assetdetails_date_added_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetdetails",
            name="date_of_purchase",
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
