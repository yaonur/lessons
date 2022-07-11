from django.urls import path
from . import views

urlpatterns = [
    path('products/frontend', views.ProductFrontendAPIView.as_view(), name='product_front'),
    path('products/backend', views.ProductBackendAPIView.as_view(), name='product_back')
]
