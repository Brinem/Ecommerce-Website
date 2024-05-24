
from django.shortcuts import redirect
from django.urls import reverse


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/place_order/' and not request.session.get('customer'):
            return redirect(reverse('login'))  # Redirect to login if not logged in and trying to place an order
        return self.get_response(request)
