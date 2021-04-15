from django.core.paginator import Paginator


def pagination(queryset, page_number, paginate_by=10):
    """function to create pagination and return a query set for page number"""
    paginator = Paginator(queryset, paginate_by)
    max_page = len(paginator.page_range)

    return [] if (max_page < int(page_number) or not queryset.exists()) else paginator.get_page(page_number)


def get_paginated_queryset_with_maxpages(queryset,page_number,paginate_by=10):

    paginator = Paginator(queryset, paginate_by)
    max_page = len(paginator.page_range)
    page_list = [] if (max_page < int(page_number) or not queryset.exists()) else paginator.get_page(page_number)

    temp = {}
    temp['page_list'] = page_list
    temp['last_page'] = paginator.num_pages
    return temp


class NumberUtilities:

    @staticmethod
    def get_integer_from_string(number_string: str, return_default: int = 0) -> int:
        try:
            return int(number_string)
        except (ValueError, TypeError):
            return return_default
