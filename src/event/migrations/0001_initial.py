# Generated by Django 5.0 on 2023-12-31 02:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("crm", "0001_initial"),
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("date", models.DateField()),
                ("description", models.TextField()),
                ("categories", models.ManyToManyField(to="inventory.category")),
                ("volunteers", models.ManyToManyField(to="crm.volunteer")),
            ],
        ),
        migrations.CreateModel(
            name="AttendeeCheckOut",
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
                ("referrer", models.CharField(max_length=100)),
                ("checkout_time", models.DateTimeField(auto_now_add=True)),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "attendee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="crm.attendee"
                    ),
                ),
                ("items", models.ManyToManyField(to="inventory.item")),
                ("volunteer", models.ManyToManyField(to="crm.volunteer")),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="event.event"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EventCheckIn",
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
                ("referrer", models.CharField(blank=True, max_length=100, null=True)),
                ("checkin_time", models.DateTimeField(auto_now_add=True)),
                (
                    "attendee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="crm.attendee"
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="event.event"
                    ),
                ),
                ("items", models.ManyToManyField(to="inventory.item")),
            ],
        ),
        migrations.CreateModel(
            name="EventTimeSlot",
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
                ("time_slot_begin", models.TimeField()),
                ("time_slot_end", models.TimeField()),
                ("openings", models.IntegerField()),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="event.event"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VolunteerTime",
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
                ("time_in", models.TimeField()),
                ("time_out", models.TimeField()),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="event.event"
                    ),
                ),
                (
                    "volunteer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="crm.volunteer"
                    ),
                ),
            ],
        ),
    ]
