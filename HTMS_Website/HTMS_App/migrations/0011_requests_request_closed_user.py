# Generated by Django 4.1.1 on 2023-01-28 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("HTMS_App", "0010_assets_image_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="requests",
            name="request_closed_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="request_closed_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
