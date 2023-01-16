# Generated by Django 4.1.1 on 2022-12-20 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("HTMS_App", "0003_technician_mobile_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="requests",
            name="request_assigned_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="requests",
            name="request_closed_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="requests",
            name="request_resolved_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
