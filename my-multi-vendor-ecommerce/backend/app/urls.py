from django.urls import path
from .views import ProductListView, VendorListView, OrderListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('vendors/', VendorListView.as_view(), name='vendor-list'),
    path('orders/', OrderListView.as_view(), name='order-list'),
]