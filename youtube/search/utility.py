from django.core.paginator import Paginator


def pagination(queryset, page_number, paginate_by=10):
    '''function to create pagination and return a query set for page number'''
    paginator = Paginator(queryset, paginate_by)
    max_page = len(paginator.page_range)

    return [] if (max_page < int(page_number) or not queryset.exists()) else paginator.get_page(page_number)