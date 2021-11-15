from django.http import HttpResponse
from .api_test import getnewposts

def my_cron_job():
    try:
        getnewposts()
    except:
        return HttpResponse("Some error encountered")