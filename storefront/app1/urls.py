from django.urls import path 
from . import views 

urlpatterns = [
    path('products/', views.all_collections),
    path('products/<int:collection_id>/<int:id>', views.single_product),
    path('products/<int:collection_id>', views.single_collection),
    path('orders/', views.all_orders),
]