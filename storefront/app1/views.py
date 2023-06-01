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
def all_collections(request):
    if request.method == 'GET':
         queryset = Collection.objects.all()
         print('hi')
         print(queryset)
         return render(request, 'all_collections.html', {"collections": queryset})
    
@api_view(['GET'])
def single_collection(request, collection_id):
    if request.method == 'GET':
         queryset = Product.objects.filter(collection_id=collection_id)
         return render(request, 'single_collection.html', {"filtered_products": queryset})

@api_view(['GET', 'POST'])
def single_product(request, collection_id, id):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=id)
 
        return render(request, 'single_product.html', {"product": product})
    
@api_view(['GET', 'POST'])
def all_orders(request):
    if request.method == 'GET':
        return render(request, 'all_orders.html')