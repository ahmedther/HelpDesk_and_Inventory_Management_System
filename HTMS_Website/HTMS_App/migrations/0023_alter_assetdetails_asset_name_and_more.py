# Generated by Django 4.1.1 on 2023-02-04 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("HTMS_App", "0022_assetdetails_last_modified_by_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetdetails",
            name="asset_name",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="asset_details",
                to="HTMS_App.assets",
            ),
        ),
        migrations.AlterField(
            model_name="assetdetails",
            name="asset_user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="assetdetails",
            name="assign_to_ticket",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assign_to_ticket",
                to="HTMS_App.requests",
            ),
        ),
        migrations.AlterField(
            model_name="assetdetails",
            name="brand",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="assetdetails",
            name="current_status",
            field=models.CharField(
                blank=True, db_index=True, default="In Stock", max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="assetdetails",
            name="date_added",
            field=models.DateTimeField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name="assetdetails",
            name="date_of_purchase",
            field=models.DateTimeField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name="assetdetails",
            name="description",
            field=models.TextField(
                blank=True, db_index=True, max_length=99999999, null=True
            ),
        ),
        migrations.AlterField(
            model_name="assetdetails",
            name="facility",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="facilities",
                to="HTMS_App.facilitydropdown",
            ),
        ),
        migrations.AlterField(
            model_name="assetdetails",
            name="last_modified_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="last_modified_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="assetdetails",
            name="model_name",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="assetdetails",
            name="model_number",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="assetdetails",
            name="serial_number",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="assets",
            name="asset_creator",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="asset_creator",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="assets",
            name="asset_description",
            field=models.TextField(
                blank=True, db_index=True, max_length=99999999, null=True
            ),
        ),
        migrations.AlterField(
            model_name="assets",
            name="asset_name",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="assets",
            name="asset_type",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="requests",
            name="description",
            field=models.TextField(
                blank=True, db_index=True, max_length=99999999, null=True
            ),
        ),
        migrations.AlterField(
            model_name="requests",
            name="request_category",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="requests",
            name="request_mode",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="requests",
            name="request_priority",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="requests",
            name="request_status",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="requests",
            name="request_type",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="requests",
            name="requester_department",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="requests",
            name="requester_designation",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="requests",
            name="requester_email",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="requests",
            name="requester_extension",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="requests",
            name="requester_name",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="requests",
            name="requester_phone_number",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="requests",
            name="requester_pr_number",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="requests",
            name="subject",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
    ]