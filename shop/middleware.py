from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class AdminMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.user.is_authenticated:
            if request.path == '/admin/' and not request.user.is_staff:
                return redirect('/')





