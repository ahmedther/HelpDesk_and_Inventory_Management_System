# Generated by Django 4.1.1 on 2023-02-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("HTMS_App", "0012_alter_assetdetails_date_added"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetdetails",
            name="date_added",
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
