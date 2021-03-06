from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status as status_codes
# Create your views here.
from rest_framework.views import APIView

from .async_tasks import *
from .serializers import SearchDetailSerializer
from .utility import pagination, NumberUtilities


class SearchView(APIView):

    def get(self, request, *args, **kwargs):

        """function returns search results based on title and descritpion it also search partial strings"""

        search_query = request.GET.get('search_query', None)

        if not search_query:
            return JsonResponse({'error_message': "Invalid search query"}, status=status_codes.HTTP_400_BAD_REQUEST)

        page = request.GET.get('page', 1)

        page = NumberUtilities.get_integer_from_string(page)

        if page == 0:
            return JsonResponse({'error_message': "Invalid page number"}, status=status_codes.HTTP_400_BAD_REQUEST)

        search_filter = self.get_query_filter(search_query)

        search_filter = pagination(search_filter, page_number=page, paginate_by=10)

        search_list = SearchDetailSerializer(search_filter, many=True).data

        return JsonResponse({'search_list': search_list}, status=status_codes.HTTP_200_OK)

    def get_query_filter(self, search_query):

        """return search filter in descending order of published at"""
        q = self.process_query(search_query)
        search_filter = SearchDetail.objects.filter(q).order_by('-published_at')

        return search_filter

    @staticmethod
    def process_query(search_string):

        """process a condition for partial string matching"""
        q = None

        for word in search_string.split():
            q_aux = Q(title__icontains=word) | Q(description__icontains=word)
            q = (q_aux & q) if bool(q) else q_aux

        return q


class FetchView(APIView):

    def get(self, request, *args, **kwargs):

        """return data in paginated format which is stored in db"""

        page = request.GET.get('page', 1)

        data_filter = SearchDetail.objects.all().order_by('-published_at')

        data_filter = pagination(data_filter, page_number=page, paginate_by=10)

        search_list = SearchDetailSerializer(data_filter, many=True).data

        return JsonResponse({'search_list': search_list}, status=status_codes.HTTP_200_OK)


class SetApiKey(APIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SetApiKey, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        """set a api key to be used to hit youtube apis also.
        This gives the support to add multiple keys if quota of one key is over"""

        api_key = request.POST.get('api_key')

        if not api_key:
            return JsonResponse({'success': False, 'error_message': "Invalid post param"},
                                status=status_codes.HTTP_400_BAD_REQUEST)

        DeveloperKeys.create_instance(api_key)

        return JsonResponse({'success': True})
