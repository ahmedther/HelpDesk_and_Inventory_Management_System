# Generated by Django 4.1.1 on 2023-01-28 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("HTMS_App", "0009_alter_assetdetails_asset_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="assets",
            name="image_url",
            field=models.CharField(db_index=True, max_length=300, null=True),
        ),
    ]