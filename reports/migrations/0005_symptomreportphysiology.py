# Generated by Django 2.2.11 on 2020-04-16 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0004_auto_20200410_2344"),
    ]

    operations = [
        migrations.CreateModel(
            name="SymptomReportPhysiology",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_source", models.TextField()),
                ("values", models.TextField()),
                (
                    "report",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reports.SymptomReport",
                    ),
                ),
            ],
        ),
    ]
