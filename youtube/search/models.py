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
