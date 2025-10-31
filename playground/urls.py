from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello),
    path("query/", views.sqlquery),
    
]