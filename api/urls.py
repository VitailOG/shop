from django.urls import path
from api.product.views import ProductAPI
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('product', ProductAPI, basename='product')

urlpatterns = [
]

urlpatterns += router.urls
