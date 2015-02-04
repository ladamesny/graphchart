import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'graphhackerati.settings')

from datetime import datetime
import requests
from graphchart.models import Reading

url = 'http://polar-dawn-2893.herokuapp.com/'

if __name__ == '__main__':
    if Reading.objects.count() > 100:
        Reading.objects.all().delete()
    res = requests.get(url).json()
    Reading.objects.get_or_create(temperature=int(res['degrees']), reading_time=datetime.now())