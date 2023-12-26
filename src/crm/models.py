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

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Volunteer(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def agreement_signed(self):
        volunteer_agreement = VolunteerAgreement.objects.filter(volunteer=self)
        if volunteer_agreement:
            return True
        return False


class VolunteerAgreement(models.Model):
    date = models.DateField()
    donation = models.FloatField()
    frequency = models.CharField(max_length=100, blank=True)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.volunteer} - {self.date}"


class VolunteerSignup(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    agreement = models.ForeignKey(VolunteerAgreement, on_delete=models.CASCADE)
    event = models.ForeignKey("event.Event", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.volunteer} - {self.agreement} - {self.event}"
