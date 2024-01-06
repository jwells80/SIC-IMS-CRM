from django.db import models


class Attendee(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    birth_gender = models.CharField(
        max_length=1, blank=True, choices=[("M", "Male"), ("F", "Female")]
    )
    homeless = models.BooleanField(default=False)
    agreement_signed = models.BooleanField(default=False)
    agreement_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AttendeeSignup(models.Model):
    time_slot = models.ForeignKey("event.EventTimeSlot", on_delete=models.CASCADE)
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)


class Volunteer(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class VolunteerAgreement(models.Model):
    volunteer = models.OneToOneField(Volunteer, on_delete=models.CASCADE)
    date = models.DateField()
    donation = models.FloatField()
    frequency = models.CharField(max_length=100, blank=True)


class VolunteerSignup(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    agreement = models.ForeignKey(VolunteerAgreement, on_delete=models.CASCADE)
    event = models.ForeignKey("event.Event", on_delete=models.CASCADE)
    time_period = models.ForeignKey("event.EventTimeSlot", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.volunteer} - {self.agreement} - {self.event}"
