# Generated by Django 4.1.7 on 2023-03-25 12:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("HTMS_App", "0035_alter_technician_mobile_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="requests",
            name="last_modified_by",
        ),
        migrations.RemoveField(
            model_name="requests",
            name="request_closed_user",
        ),
        migrations.RemoveField(
            model_name="requests",
            name="request_submitter",
        ),
        migrations.RemoveField(
            model_name="requests",
            name="request_technician",
        ),
        migrations.DeleteModel(
            name="AssetDetails",
        ),
        migrations.DeleteModel(
            name="Requests",
        ),
    ]
