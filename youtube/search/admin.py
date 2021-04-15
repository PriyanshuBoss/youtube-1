from django.contrib import admin

# Register your models here.
from .models import SearchDetail, DeveloperKeys

admin.site.register(SearchDetail)
admin.site.register(DeveloperKeys)
