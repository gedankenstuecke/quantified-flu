# Generated by Django 2.2.11 on 2020-03-31 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("retrospective", "0004_retrospectiveevent_notes")]

    operations = [
        migrations.AlterField(
            model_name="retrospectiveevent",
            name="notes",
            field=models.TextField(
                blank=True,
                help_text="Notes about this illness, e.g. do you know or believe it was a cold, flu, or coronavirus infection?",
            ),
        )
    ]