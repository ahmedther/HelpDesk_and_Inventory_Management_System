# Generated by Django 4.1.1 on 2023-02-02 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("HTMS_App", "0021_alter_assetdetails_current_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="assetdetails",
            name="last_modified_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="last_modified_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="assetdetails",
            name="last_modified_date",
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name="requests",
            name="last_modified_date",
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
    ]
