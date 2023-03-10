# Generated by Django 4.1.7 on 2023-02-20 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("HTMS_App", "0033_alter_assetdetails_date_of_purchase"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetdetails",
            name="facility",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="facilities",
                to="HTMS_App.facilitydropdown",
            ),
        ),
    ]
