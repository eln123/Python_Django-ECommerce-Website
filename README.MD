Overview of what I have done:

    1) Make a git init file and add any SECRETS to it
    2) pip3 install django in folder you want
    3) Create a project
          - django-admin startproject name-of-project (I did "storefront")
    4) Create an app
          - python3 manage.py startapp name-of-app (I did "app1")
          - ** I added 'app1' to INSTALLED_APPS list in settings.py
    5) Then map up your app1 urls to your urls.py in storefront
```python

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),
]

   ```
    1) Then created a templates folder in app1 repo
    2) Added html file to it
    3) Then I used render function in app1/views.py to render html.template file

```python 

from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def test(request):
    return render(request, 'hello.html', {"name": "Ethan"})

```

    9) Created models in models.py
    10) Ran makemigrations and migrate
    11) Linked CSS to html files
    12) What I want website to look like:

Endpoints: 

/products
https://www.wholefoodsmarket.com/products

/products/collection
https://www.wholefoodsmarket.com/products/dairy-eggs

/products/single-product
https://www.wholefoodsmarket.com/product/maple-hill-creamery-organic-whole-milk-b06zynz7nf


     ## Bugs:
    - My static css files were not updating properly
    - I added this code to settings.py:
```python
     STATIC_URL = '/app1/static/'
 ```

    instead of:
    
``` python
    STATIC_URL = '/static/'
```