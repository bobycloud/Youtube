from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<str:url_hash>/', views.redirect_url, name='redirect_url'),
]
