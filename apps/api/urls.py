from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path(
        route='categories/',
        view=views.CategoryListCreateApiView.as_view()
    ),
    path(
        route='category/<str:slug>/',
        view=views.CategoryEditDeleteApiView.as_view()
    ),
    path(
        route='products/',
        view=views.ProductListCreateApiView.as_view()
    ),
    path(
        route='product/<str:slug>/',
        view=views.ProductEditDeleteApiView.as_view()
    ),
    path(
        route='product-images/',
        view=views.ProductImageListCreateApiView.as_view()
    ),
    path(
        route='product-image/<int:pk>/',
        view=views.ProductImageEditDeleteApiView.as_view()
    ),
    path(
        route='inventories/',
        view=views.InventoryListCreateApiView.as_view()
    ),
    path(
        route='inventory/<int:pk>/',
        view=views.InventoryEditDeleteApiView.as_view()
    ),
    path(
        route='customers/',
        view=views.CustomerListCreateApiView.as_view()
    ),
    path(
        route='customer/<int:pk>/',
        view=views.CustomerEditDeleteApiView.as_view()
    ),
    path(
        route='orders/',
        view=views.OrderListCreateApiView.as_view()
    ),
    path(
        route='order/<int:pk>/',
        view=views.OrderEditDeleteApiView.as_view()
    )
]