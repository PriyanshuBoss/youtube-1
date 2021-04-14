from .constants import *
from googleapiclient.discovery import build
from .models import SearchDetail


def fill_data_from_youtube():

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(q=QUERY, part='id,snippet', maxResults=20, order='date',
                                            publishedAfter='2010-01-01T00:00:00Z').execute()

    for item in search_response['items']:
        datetime = item['snippet']['publishedAt']
        description = item['snippet']['description']
        title = item['snippet']['title']
        thumbnail = item['snippet']['thumbnails']['default']['url']

        obj, created = SearchDetail.objects.update_or_create(
            title=title, thumbnail=thumbnail,
            defaults={'datetime': datetime, 'description': description}
        )
