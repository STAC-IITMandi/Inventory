from django.urls import path

from . import views


urlpatterns = [
    path('', views.inventory, name="inventory"),
    path('new/', views.new, name='new'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
