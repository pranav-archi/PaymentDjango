from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('create-order/', views.create_order, name='create_order'),
]