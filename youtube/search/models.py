from django.db import models


class SearchDetail(models.Model):
    # video title
    title = models.CharField(max_length=4096, null=False)
    description = models.TextField(null=True)
    thumbnail = models.URLField()
    datetime = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.title)
