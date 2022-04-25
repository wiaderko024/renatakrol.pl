from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(default="", blank=False, null=False)
    time = models.DateTimeField(blank=False, null=False)
    place = models.TextField(default="", blank=False, null=False)
    polish_date = models.CharField(max_length=128, blank=True, null=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        day = self.time.day
        month = self.time.month.numerator
        year = self.time.year
        time = self.time.time().isoformat().split(':')
        hour = time[0]
        minute = time[1]

        if month == 1:
            month = 'Styczeń'
        elif month == 2:
            month = 'Luty'
        elif month == 3:
            month = 'Marzec'
        elif month == 4:
            month = 'Kwiecień'
        elif month == 5:
            month = 'Maj'
        elif month == 6:
            month = 'Czerwiec'
        elif month == 7:
            month = 'Lipiec'
        elif month == 8:
            month = 'Sierpień'
        elif month == 9:
            month = 'Wrzesień'
        elif month == 10:
            month = 'Październik'
        elif month == 11:
            month = 'Listopad'
        elif month == 12:
            month = 'Grudzień'

        self.polish_date = str(f"{day} {month} {year} - {hour}:{minute}")

        return super(Event, self).save(*args, **kwargs)
