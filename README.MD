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
    6) Then created a templates folder in your app1 repo
    7) Added html file to it
    8) Then I used render function in app1/views.py to render html.template file

```python 

from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def test(request):
    return render(request, 'hello.html', {"name": "Ethan"})

```

    9) Created models in models.py
    10) Ran makemigrations and migrate to 