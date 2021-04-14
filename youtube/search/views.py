from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status as status_codes
# Create your views here.

from .async_tasks import *
from .serializers import SearchDetailSerializer
from .utility import pagination


def search(request):
    title = request.GET.get('title')
    description = request.GET.get('description')

    page = request.GET.get('page', 1)

    search_filter = SearchDetail.objects.filter(title=title, description=description).order_by('-datetime')

    search_filter = pagination(search_filter, page_number=page, paginate_by=10)

    search_list = SearchDetailSerializer(search_filter, many=True).data

    return JsonResponse({'search_list': search_list}, status=status_codes.HTTP_200_OK)


def fetch_data(request):

    page = request.GET.get('page', 1)

    data_filter = SearchDetail.objects.all().order_by('-datetime')

    data_filter = pagination(data_filter, page_number=page, paginate_by=10)

    search_list = SearchDetailSerializer(data_filter, many=True).data

    return JsonResponse({'search_list': search_list}, status=status_codes.HTTP_200_OK)