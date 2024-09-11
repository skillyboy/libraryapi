from django.contrib import  admin
from django.urls import path, include 
from books.api import api  # Import the `api` object from `books.api`

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),  # Use the API routes defined in `books/api.py`
]
