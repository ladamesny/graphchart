import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'graphhackerati.settings')

import django

from datetime import datetime
from graphchart.models import Reading

def populate():
    Reading.objects.get_or_create(temperature=55, reading_time=datetime.utcnow())
    Reading.objects.get_or_create(temperature=60, reading_time=datetime.utcnow())
    Reading.objects.get_or_create(temperature=65, reading_time=datetime.utcnow())
    Reading.objects.get_or_create(temperature=60, reading_time=datetime.utcnow())
    Reading.objects.get_or_create(temperature=62, reading_time=datetime.utcnow())
    Reading.objects.get_or_create(temperature=51, reading_time=datetime.utcnow())
    Reading.objects.get_or_create(temperature=48, reading_time=datetime.utcnow())
    Reading.objects.get_or_create(temperature=45, reading_time=datetime.utcnow())
    Reading.objects.get_or_create(temperature=40, reading_time=datetime.utcnow())
    Reading.objects.get_or_create(temperature=48, reading_time=datetime.utcnow())

if __name__ == '__main__':
    print("Starting Graph Chart Population script")
    populate()