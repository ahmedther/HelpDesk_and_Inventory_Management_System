# Generated by Django 4.1.1 on 2023-02-02 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("HTMS_App", "0013_alter_assetdetails_date_added"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetdetails",
            name="date_added",
            field=models.DateField(auto_now_add=True, db_index=True),
        ),
    ]
