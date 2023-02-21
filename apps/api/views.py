from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductImagesSerializer,
    InventorySerializer,
    CustomerSerializer,
    OrderSerializer,
)
from product.models import (
    Category,
    Product,
    ProductImages,
    Inventory,
    Customer,
    Order
)


# Category
class CategoryListCreateApiView(APIView):
    serializer_class = CategorySerializer
    model = Category

    def get(self, request, *args, **kwargs):
        categories = self.model.objects.all()
        serializer = self.serializer_class(instance=categories, many=True)
        return Response(data=serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)


class CategoryEditDeleteApiView(APIView):
    serializer_class = CategorySerializer
    model = Category

    def get(self, request, slug, *args, **kwargs):
        category = get_object_or_404(self.model, slug=slug)
        serializer = self.serializer_class(instance=category)
        return Response(data=serializer.data, status=200)

    def put(self, request, slug, *args, **kwargs):
        data = request.data
        category = get_object_or_404(self.model, slug=slug)
        serializer = self.serializer_class(instance=category, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)

    def patch(self, request, slug, *args, **kwargs):
        data = request.data
        category = get_object_or_404(self.model, slug=slug)
        serializer = self.serializer_class(instance=category, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)

    def delete(self, request, slug, *args, **kwargs):
        pass


# Product
class ProductListCreateApiView(APIView):
    serializer_class = ProductSerializer
    model = Product

    def get(self, request, *args, **kwargs):
        products = self.model.objects.all()
        serializer = self.serializer_class(instance=products, many=True)
        return Response(data=serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)


class ProductEditDeleteApiView(APIView):
    serializer_class = ProductSerializer
    model = Product

    def get(self, request, slug, *args, **kwargs):
        product = get_object_or_404(self.model, slug=slug)
        serializer = self.serializer_class(instance=product)
        return Response(data=serializer.data, status=200)

    def put(self, request, slug, *args, **kwargs):
        data = request.data
        product = get_object_or_404(self.model, slug=slug)
        serializer = self.serializer_class(instance=product, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)

    def patch(self, request, slug, *args, **kwargs):
        data = request.data
        product = get_object_or_404(self.model, slug=slug)
        serializer = self.serializer_class(instance=product, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)

    def delete(self, request, slug, *args, **kwargs):
        category = get_object_or_404(self.model, slug=slug)
        category_id = category.id
        category.delete()
        return Response(data={'deleted': f'{category_id} - Category deleted successfully!'}, status=204)


# Product Image
class ProductImageListCreateApiView(APIView):
    serializer_class = ProductImagesSerializer
    model = ProductImages

    def get(self, request, *args, **kwargs):
        productImages = self.model.objects.all()
        serializer = self.serializer_class(instance=productImages, many=True)
        return Response(data=serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)


class ProductImageEditDeleteApiView(APIView):
    serializer_class = ProductImagesSerializer
    model = ProductImages

    def get(self, request, pk, *args, **kwargs):
        productImage = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(instance=productImage)
        return Response(data=serializer.data, status=200)

    def put(self, request, pk, *args, **kwargs):
        data = request.data
        productImage = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(instance=productImage, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)

    def patch(self, request, pk, *args, **kwargs):
        data = request.data
        productImage = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(instance=productImage, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)

    def delete(self, request, slug, *args, **kwargs):
        product = get_object_or_404(self.model, slug=slug)
        product_id = product.id
        product.delete()
        return Response(data={'deleted': f'{product_id} - Product deleted successfully!'}, status=204)


# Inventory
class InventoryListCreateApiView(APIView):
    serializer_class = InventorySerializer
    model = Inventory

    def get(self, request, *args, **kwargs):
        inventories = self.model.objects.all()
        serializer = self.serializer_class(instance=inventories, many=True)
        return Response(data=serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)


class InventoryEditDeleteApiView(APIView):
    serializer_class = InventorySerializer
    model = Inventory

    def get(self, request, pk, *args, **kwargs):
        inventory = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(instance=inventory)
        return Response(data=serializer.data, status=200)

    def put(self, request, pk, *args, **kwargs):
        data = request.data
        inventory = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(instance=inventory, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)

    def patch(self, request, pk, *args, **kwargs):
        data = request.data
        inventory = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(instance=inventory, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)

    def delete(self, request, pk, *args, **kwargs):
        inventory = get_object_or_404(self.model, pk=pk)
        inventory_id = inventory.id
        inventory.delete()
        return Response(data={'deleted': f'{inventory_id} - Inventory deleted successfully!'}, status=204)


# Customer
class CustomerListCreateApiView(APIView):
    serializer_class = CustomerSerializer
    model = Customer

    def get(self, request, *args, **kwargs):
        customers = self.model.objects.all()
        serializer = self.serializer_class(instance=customers, many=True)
        return Response(data=serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)


class CustomerEditDeleteApiView(APIView):
    serializer_class = CustomerSerializer
    model = Customer

    def get(self, request, pk, *args, **kwargs):
        customer = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(instance=customer)
        return Response(data=serializer.data, status=200)

    def put(self, request, pk, *args, **kwargs):
        data = request.data
        customer = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(instance=customer, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)

    def patch(self, request, pk, *args, **kwargs):
        data = request.data
        customer = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(instance=customer, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)

    def delete(self, request, pk, *args, **kwargs):
        customer = get_object_or_404(self.model, pk=pk)
        customer_id = customer.id
        customer.delete()
        return Response(data={'deleted': f'{customer_id} - Customer deleted successfully!'}, status=204)


# Order
class OrderListCreateApiView(APIView):
    serializer_class = OrderSerializer
    model = Order

    def get(self, request, *args, **kwargs):
        orders = self.model.objects.all()
        serializer = self.serializer_class(instance=orders, many=True)
        return Response(data=serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)


class OrderEditDeleteApiView(APIView):
    serializer_class = OrderSerializer
    model = Order

    def get(self, request, pk, *args, **kwargs):
        order = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data, status=200)

    def put(self, request, pk, *args, **kwargs):
        data = request.data
        order = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(instance=order, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)

    def patch(self, request, pk, *args, **kwargs):
        data = request.data
        order = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(instance=order, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)

    def delete(self, request, pk, *args, **kwargs):
        order = get_object_or_404(self.model, pk=pk)
        order_id = order.id
        order.delete()
        return Response(data={'deleted': f'{order_id} - Order deleted successfully!'}, status=204)