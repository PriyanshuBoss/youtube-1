from django.shortcuts import render

# Create your views here.
from search.models import SearchDetail
from search.serializers import SearchDetailSerializer
from search.utility import pagination


def dashboard(request):
    page = request.GET.get('page', 1)

    data_filter = SearchDetail.objects.order_by('-published_at')

    data_filter = pagination(data_filter, page, paginate_by=10)

    data_list = SearchDetailSerializer(data_filter, many=True).data

    return render(request, 'dashboard.html', {'data_list': data_list})
