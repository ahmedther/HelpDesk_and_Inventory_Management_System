# Generated by Django 4.1.1 on 2023-02-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("HTMS_App", "0029_location_assetdetails_location"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="assetdetails",
            name="location",
        ),
        migrations.AddField(
            model_name="requests",
            name="location",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
    ]
