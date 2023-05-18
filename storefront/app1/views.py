from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Collection, Product, CartItem, Cart
from django.shortcuts import get_object_or_404
from django.db.models import Value
from rest_framework.decorators import api_view
from .serializers import ProductSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def all_products(request):
    if request.method == 'GET':
         queryset = Product.objects.all()
         return render(request, 'products.html', {"products": queryset})

@api_view(['GET', 'POST'])
def single_product(request, id):
    if request.method == 'GET':
        print(request)
        print('GET')
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(id)
    elif request.method == 'POST':
        print('POST')
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        # I need to redirect 
        return redirect(all_products)
        return render(request, 'single_product.html', {"product": serializer})