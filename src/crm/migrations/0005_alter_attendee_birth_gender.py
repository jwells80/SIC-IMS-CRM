# Generated by Django 5.0 on 2023-12-31 02:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crm", "0004_rename_sex_attendee_birth_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendee",
            name="birth_gender",
            field=models.CharField(
                blank=True, choices=[("M", "Male"), ("F", "Female")], max_length=1
            ),
        ),
    ]
