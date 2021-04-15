from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from search.models import SearchDetail
from search.serializers import SearchDetailSerializer
from search.utility import pagination,NumberUtilities,get_paginated_queryset_with_maxpages


def dashboard(request):

    """this function returns the stored videos in form of dashboard in paginated format"""

    page = request.GET.get('page', 1)

    page = NumberUtilities.get_integer_from_string(page)

    if page <= 0:
        return HttpResponse("invalid page number")

    data_filter = SearchDetail.objects.order_by('-published_at')

    paginated_response = get_paginated_queryset_with_maxpages(data_filter, page, paginate_by=10)
    data_filter = paginated_response['page_list']
    last_page = paginated_response['last_page']
    data_list = SearchDetailSerializer(data_filter, many=True).data

    if last_page < page:
        return HttpResponse("invalid page number")

    return render(request, 'dashboard.html', {'data_list': data_list, 'page': page})

