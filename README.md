# youtube_fetch_api_django
To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

mysite contains:  
1. Screenshots       # Contain screenshots of the project and other images
2. api               # The main Django app/api containing the models, views, serializers etc
3. fetch_api         # All the settings and url routes settings of the REST API
4. db.sqlite3        # SQLite database housing the data of the videos fetched
5. manage.py         # Python code used for starting the app by establishing DRF server
6. requirements.txt  # Requirements file


## Clone the repo and install Requirements:
1. git clone
2. cd mysite
3. pip3 install -r requirements.txt (Install the requirements preferrably in Virtual environment)

## Modify settings.py File - Remove the existing keys and add your own YouTube Data API keys in the form
API_KEYS = ['Google_API_Key_1', 'Google_API_Key_2','Google_API_Key_3',] 

## Steps to run
### Run the manage.py file:
python3 manage.py runserver

### To fetch new videos, visit the '/new' endpoint:
open http://127.0.0.1:8000/new to fetch the new videos in paginated and reverse chronological format

###For watching added videos
open http://127.0.0.1:8000 to see all the fetched videos related to cricket query posted in the past 5 minutes.
