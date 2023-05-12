# Generated by Django 4.1.7 on 2023-04-05 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("HTMS_App", "0037_requests_assetdetails"),
    ]

    operations = [
        migrations.AlterField(
            model_name="technician",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="techinican",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]