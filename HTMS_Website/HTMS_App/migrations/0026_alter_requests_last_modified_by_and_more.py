# Generated by Django 4.1.1 on 2023-02-04 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("HTMS_App", "0025_alter_requests_request_submitter_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="requests",
            name="last_modified_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="updater",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="technician",
            name="facility",
            field=models.ManyToManyField(
                blank=True, db_index=True, null=True, to="HTMS_App.facilitydropdown"
            ),
        ),
        migrations.AlterField(
            model_name="technician",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("Male", "Male"), ("Female", "Female")],
                max_length=6,
            ),
        ),
    ]
