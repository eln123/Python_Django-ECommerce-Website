from django.urls import path 
from . import views 

urlpatterns = [
    path('products/', views.all_products),
     path('products/<int:id>', views.single_product)
] 