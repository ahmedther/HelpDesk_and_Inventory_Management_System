# Generated by Django 4.1.1 on 2023-01-17 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("HTMS_App", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Assest_Details",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("brand", models.CharField(db_index=True, max_length=100, null=True)),
                (
                    "model_name",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
                (
                    "model_number",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
                (
                    "serial_number",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
                (
                    "date_of_purchase",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                ("date_added", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "current_status",
                    models.CharField(
                        choices=[
                            ("in-stock", "In Stock"),
                            ("in-use", "In Use"),
                            ("returned_to_vendor", "Returned To Vendor"),
                            ("lost", "Lost"),
                        ],
                        db_index=True,
                        default="in-stock",
                        max_length=20,
                    ),
                ),
                (
                    "description",
                    models.TextField(db_index=True, max_length=99999999, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Assets",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "assest_name",
                    models.CharField(db_index=True, max_length=100, unique=True),
                ),
                (
                    "assest_creation_date",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    "assest_type",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
                (
                    "assest_description",
                    models.TextField(db_index=True, max_length=99999999, null=True),
                ),
                (
                    "asset_creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="asset_creator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewIncidentCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category_name",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
                (
                    "subcategory_name",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewIncidentMode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "mode_name",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewIncidentPriority",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "priority_name",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewIncidentRequestType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "request_name",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewIncidentStatus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status_name",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Requests",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "requester_name",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
                (
                    "requester_pr_number",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
                (
                    "requester_designation",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
                (
                    "requester_department",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
                (
                    "requester_email",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
                (
                    "requester_extension",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
                (
                    "requester_phone_number",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
                (
                    "request_type",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
                (
                    "request_status",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
                (
                    "request_mode",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
                (
                    "request_priority",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
                (
                    "request_category",
                    models.CharField(db_index=True, max_length=100, null=True),
                ),
                ("subject", models.CharField(db_index=True, max_length=100, null=True)),
                (
                    "description",
                    models.TextField(db_index=True, max_length=99999999, null=True),
                ),
                (
                    "request_creation_date",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    "request_completion_date",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                (
                    "last_modified_date",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    "request_assigned_time",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                (
                    "request_resolved_time",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                (
                    "request_closed_time",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                (
                    "last_modified_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="updater",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "request_submitter",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="creator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "request_technician",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assignee",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Technician",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "department",
                    models.CharField(
                        blank=True, db_index=True, max_length=100, null=True
                    ),
                ),
                (
                    "designation",
                    models.CharField(
                        blank=True, db_index=True, max_length=100, null=True
                    ),
                ),
                ("pr_number", models.CharField(db_index=True, max_length=100)),
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")], max_length=6
                    ),
                ),
                (
                    "mobile_number",
                    models.CharField(
                        blank=True, db_index=True, max_length=10, null=True
                    ),
                ),
                (
                    "extension_number",
                    models.CharField(
                        blank=True, db_index=True, max_length=10, null=True
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="facilitydropdown",
            name="facility_code",
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="facilitydropdown",
            name="facility_name",
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.DeleteModel(
            name="Employee",
        ),
        migrations.AddField(
            model_name="technician",
            name="facility",
            field=models.ManyToManyField(to="HTMS_App.facilitydropdown"),
        ),
        migrations.AddField(
            model_name="technician",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="assest_details",
            name="assest_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assest_details",
                to="HTMS_App.assets",
            ),
        ),
        migrations.AddField(
            model_name="assest_details",
            name="assest_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="assest_details",
            name="assign_to_ticket",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assign_to_ticket",
                to="HTMS_App.requests",
            ),
        ),
        migrations.AddField(
            model_name="assest_details",
            name="facility",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="facilities",
                to="HTMS_App.facilitydropdown",
            ),
        ),
    ]