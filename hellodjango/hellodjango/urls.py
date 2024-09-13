from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("hello/", views.hello),
    path("add/", views.add),
    path("sub/", views.sub),
    path("result/", views.dict),
    path("hospital/", views.hospital),
]
