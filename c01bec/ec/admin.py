from django.contrib import admin

# Register your models here.
from .models import Products, Orders, OrderDetails, Cart

admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(OrderDetails)
admin.site.register(Cart)
# Compare this snippet from c01bec/ec/views.py:
# from django.shortcuts import render
# from django.http import HttpResponse
# 
# # Create your views here.
# def index(request):
#     return HttpResponse("Hello, world.")
# Compare this snippet from c01bec/ec/urls.py:
# from django.urls import path
# 
# from . import views
# 
# urlpatterns = [
#     path('', views.index, name='index'),
# ]
# Compare this snippet from c01bec/ec/apps.py:
# from django.apps import AppConfig
# 
# 
# class EcConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'ec'
# Compare this snippet from c01bec/ec/views.py:
# from django.shortcuts import render
# from django.http import HttpResponse
# 
# # Create your views here.
# def index(request):
#     return HttpResponse("Hello, world.")
# Compare this snippet from c01bec/ec/urls.py:
# from django.urls import path
# 
# from . import views
# 
# urlpatterns = [
#     path('', views.index, name='index'),
# ]
# Compare this snippet from c01bec/ec/apps.py:
# from django.apps import AppConfig
# 
# 
# class EcConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'ec'
# Compare this snippet from c01bec/ec/views.py:
# from django.shortcuts import render
# from django.http import HttpResponse
# 
# # Create your views here.
# def index(request):
#     return HttpResponse("Hello, world.")
# Compare this snippet from c01bec/ec/urls.py:
# from django.urls import path
# 
# from . import views
# 
# urlpatterns = [
#     path('', views.index, name='index'),
# ]
# Compare this snippet from c01bec/ec/apps.py:
# from django.apps import AppConfig
# 
# 
# class EcConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'ec'
# Compare this snippet from c01bec/ec/views.py:
# from django.shortcuts import render
# from