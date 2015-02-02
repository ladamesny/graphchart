import datetime

from django.db import models
from django.utils import timezone

class Reading(models.Model):
    temperature = models.IntegerField(default=0)
    reading_time = models.DateTimeField('time of reading')

    def __str__(self):
        name = str(self.id)
        return name

    def was_read_recently(self):
        now = timezone.now()
        return now- datetime.timedelta(hours=1) <= self.reading_time<= now
        was_read_recently.admin_order_field = 'reading_time'
        was_read_recently.boolean = True
        was_read_recently.short_descrtion = 'Read recently?'

