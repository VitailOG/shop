from django.urls import path
from api.product.views import CategoryAPI, ProductAPI
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('category-api', CategoryAPI)
router.register('product', ProductAPI)

urlpatterns = [
]

urlpatterns += router.urls
