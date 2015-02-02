import json
import urllib, urllib2

def run_query(search_terms):

    root_url = 'https://polar-dawn-2893.herokuapp.com/'
    try:
        response = urllib2.urlopen(root_url).read()
        json_response = json.loads(response)

        Reading.objects.get_or_create(temperature=json_response['degrees'], reading_time=datetime.utcnow())

    except urllib2.URLError, e:
        print("Error when quering reading")