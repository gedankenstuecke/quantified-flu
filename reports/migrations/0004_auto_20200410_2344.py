# Generated by Django 2.2.11 on 2020-04-10 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("reports", "0003_symptomreportsymptomitem")]

    operations = [
        migrations.AlterField(
            model_name="symptom",
            name="label",
            field=models.CharField(
                choices=[
                    ("cough", "Cough"),
                    ("wet_cough", "Cough with mucus (phlegm)"),
                    ("anosmia", "Reduced sense of smell (anosmia)"),
                    ("runny_nose", "Runny or stuffy nose"),
                    ("sore_throat", "Sore throat"),
                    ("short_breath", "Shortness of breath"),
                    ("diarrhea", "Diarrhea"),
                    ("nausea", "Nausea or vomiting"),
                    ("chills", "Chills and sweats"),
                    ("fatigue", "Fatigue and malaise"),
                    ("headache", "Headache"),
                    ("body_ache", "Muscle pains and body aches"),
                ],
                max_length=20,
                unique=True,
            ),
        )
    ]
