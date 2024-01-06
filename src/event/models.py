from django.db import models


class Event(models.Model):
    date = models.DateField()
    description = models.TextField()
    volunteers = models.ManyToManyField("crm.Volunteer")
    categories = models.ManyToManyField("inventory.Category")
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.date


class EventTimeSlot(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    time_slot_begin = models.TimeField()
    time_slot_end = models.TimeField()
    openings = models.IntegerField()


class EventCheckIn(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey("crm.Attendee", on_delete=models.CASCADE)
    referrer = models.CharField(max_length=100, null=True, blank=True)
    checkin_time = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField("inventory.Item")

    def __str__(self):
        return self.event


# TODO: Attendee check in / Reception view


class AttendeeCheckOut(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey("crm.Attendee", on_delete=models.CASCADE)
    volunteer = models.ManyToManyField("crm.Volunteer")
    referrer = models.CharField(max_length=100)
    checkout_time = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField("inventory.Item")
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.event


class VolunteerTime(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    volunteer = models.ForeignKey("crm.Volunteer", on_delete=models.CASCADE)
    time_in = models.TimeField()
    time_out = models.TimeField()

    def __str__(self):
        return f"{self.event } - {self.volunteer}"
