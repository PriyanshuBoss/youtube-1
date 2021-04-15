from datetime import datetime

from .constants import *
from googleapiclient.discovery import build
from .models import SearchDetail, DeveloperKeys
import json

from youtube.celery import app


def get_api_fail_reason(error):
    reason = ""

    try:
        error_response = json.loads(error[1])
        reason = error_response['error']['errors'][0]['reason']

    except Exception as e:
        print(e.args)

    return reason


def get_publishing_data_after():
    """returns the published datetime after the youtube video gives data"""

    publish_datetime = '2015-01-01T00:00:00Z'

    latest_key = SearchDetail.objects.all().order_by('-published_at')[:1]

    if latest_key:
        # return the maximum datetime value from db in order to get the new data
        publish_datetime = latest_key[0].published_at.strftime('%Y-%m-%dT%H:%M:%SZ')

    return publish_datetime


def process_api_response(api_response):

    """process the response of api and save it in db"""

    if not api_response:
        return

    for item in api_response['items']:
        published_at = item['snippet']['publishedAt']
        description = item['snippet']['description']
        title = item['snippet']['title']
        thumbnail = item['snippet']['thumbnails']['default']['url']
        instance = SearchDetail.create_instance(title, thumbnail, description, published_at)


@app.task
def fill_data_from_youtube():
    """This functions hits api after 10 seconds and fill the data according to the new videos uploaded"""

    api_response = {}

    # get the valid developer key from db whose quota is not expired
    developer_filter = DeveloperKeys.objects.filter(quota_expired=False).order_by('-id')

    for instance in developer_filter:
        developer_key = instance.developer_key

        try:
            publish_datetime = get_publishing_data_after()
            youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=developer_key)
            api_response = youtube.search().list(q=QUERY, part='id,snippet', maxResults=MAX_RESULTS, order='date',
                                                 publishedAfter=publish_datetime).execute()
            print(api_response)
            break

        except Exception as e:

            error_reason = get_api_fail_reason(e.args)

            if error_reason == "quotaExceeded":
                # set the quota expired at true if the quota exceeded
                instance.quota_expired = True
                instance.save()

    process_api_response(api_response)
