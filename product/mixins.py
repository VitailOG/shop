from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin
from .models import Category, Cart, Customer


class CommonMixin(SingleObjectMixin):
    """Mixin for showing category"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CartMixin(View):
    """Mixin for basket"""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:

            customer = Customer.objects.filter(user=request.user).first()
            cart = Cart.objects.filter(customer=customer, in_order=False).first()
            if not customer:
                customer = Customer.objects.create(
                    user=request.user
                )

            if not cart:
                cart = Cart.objects.create(
                    customer=customer
                )
            self.customer = customer
        else:
            cart = None

        self.cart = cart
        return super().dispatch(request, *args, **kwargs)
