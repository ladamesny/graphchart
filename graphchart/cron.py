import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'graphhackerati.settings')
import django
import kronos
import random
from datetime import datetime
import requests
from graphchart.models import Reading

@kronos.register('*/5 * * * *')

def my_scheduled_job():
    url = 'https://polar-dawn-2893.herokuapp.com/'
    res = requests.get(url).json()
    Reading.objects.get_or_create(temperature=int(res['degrees']), reading_time=datetime.utcnow())
    pass
