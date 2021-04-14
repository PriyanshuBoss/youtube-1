from rest_framework import serializers
from .models import SearchDetail


class SearchDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SearchDetail
        fields = ('title', 'description', 'thumbnail', 'datetime')
