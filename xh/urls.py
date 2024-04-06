from django.contrib import admin
from django.urls import path
from mainaApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
]
