from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status as status_codes
# Create your views here.
from rest_framework.views import APIView

from .async_tasks import *
from .serializers import SearchDetailSerializer
from .utility import pagination


class SearchView(APIView):

    def get(self, request, *args, **kwargs):

        search_query = request.GET.get('search_query', None)
        
        if not search_query:
            return JsonResponse({'error_message': "Invalid search query"}, status=status_codes.HTTP_400_BAD_REQUEST)

        page = request.GET.get('page', 1)

        search_filter = SearchDetail.objects.filter(Q(title__icontains=search_query) |
                                                    Q(description__icontains=search_query)).order_by('-datetime')

        search_filter = pagination(search_filter, page_number=page, paginate_by=10)

        search_list = SearchDetailSerializer(search_filter, many=True).data

        return JsonResponse({'search_list': search_list}, status=status_codes.HTTP_200_OK)


class FetchView(APIView):

    def get(self, request, *args, **kwargs):
        page = request.GET.get('page', 1)

        data_filter = SearchDetail.objects.all().order_by('-datetime')

        data_filter = pagination(data_filter, page_number=page, paginate_by=10)

        search_list = SearchDetailSerializer(data_filter, many=True).data

        return JsonResponse({'search_list': search_list}, status=status_codes.HTTP_200_OK)
