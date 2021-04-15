from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# this file set celery and celery beat config for running async tasks

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube.settings')

app = Celery('youtube')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.beat_schedule = {

    'hit_youtube': {
        'task': 'search.async_tasks.fill_data_from_youtube',
        'schedule': 10,
    }
}
app.conf.timezone = 'Asia/Kolkata'

