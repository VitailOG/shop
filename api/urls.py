from django.urls import path
from api.product.views import ProductAPI#, ReviewAPI
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('product', ProductAPI, basename='product')
# router.register('review', ReviewAPI, basename='review')

urlpatterns = [
]

urlpatterns += router.urls
