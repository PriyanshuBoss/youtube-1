
from datetime import datetime
from .constants import *
from googleapiclient.discovery import build
from .models import SearchDetail


def fill_data_from_youtube():

    try:
        publish_datetime = get_publishing_data_after()
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
        search_response = youtube.search().list(q=QUERY, part='id,snippet', maxResults=100, order='date',
                                                publishedAfter=publish_datetime).execute()
    except Exception as e:
        print(e)

        return

    for item in search_response['items']:
        published_at = item['snippet']['publishedAt']
        description = item['snippet']['description']
        title = item['snippet']['title']
        thumbnail = item['snippet']['thumbnails']['default']['url']
        instance = SearchDetail.create_instance(title, thumbnail, description, published_at)



def get_publishing_data_after():
    publish_datetime = '2015-01-01T00:00:00Z'

    latest_key = SearchDetail.objects.all().order_by('-datetime')[:1]

    if latest_key:
        publish_datetime = latest_key[0].datetime.strftime('%Y-%m-%dT%H:%M:%SZ')

    return publish_datetime

