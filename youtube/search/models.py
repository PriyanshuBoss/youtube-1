import time

from django.db import models


class SearchDetail(models.Model):
    # video title
    title = models.CharField(max_length=4096, null=False)
    description = models.TextField(null=True)
    thumbnail = models.URLField()
    published_at = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.title)

    @staticmethod
    def create_instance(title, thumbnail, description, datetime):

        search_filter = SearchDetail.objects.filter(title=title, description=description)

        if not search_filter.exists():
            instance = SearchDetail()
            instance.title = title
            instance.description = description
            instance.thumbnail = thumbnail
            instance.published_at = datetime
            instance.save()


class DeveloperKeys(models.Model):

    developer_key = models.TextField()
    quota_expired = models.BooleanField(default=False)
    created_at = models.BigIntegerField(default=0)

    @staticmethod
    def create_instance(developer_key):
        key_filter = DeveloperKeys.objects.filter(developer_key=developer_key)

        if not key_filter.exists():
            instance = DeveloperKeys()
            instance.developer_key = developer_key
            instance.created_at = time.time()
            instance.save()

