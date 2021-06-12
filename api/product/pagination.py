from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    """ Pagination for model Product
    """
    page_size = 1
    max_page_size = 10

