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
1. git clone https://github.com/Apocalyptic04/youtube_fetch_api_django.git
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

## Screenshots
![Screenshot 2021-11-15 231941](https://user-images.githubusercontent.com/65764814/141837099-10ee0b3d-91a6-4997-8e82-23841f5297d3.png)

![Screenshot 2021-11-15 232045](https://user-images.githubusercontent.com/65764814/141837141-7736a54b-8f9b-432c-8d33-09fee7506523.png)

![Screenshot 2021-11-15 232113](https://user-images.githubusercontent.com/65764814/141837153-2eae1865-2a34-45c1-99ba-89ea7ea4f035.png)

