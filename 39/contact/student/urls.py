from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_contact, name='add_contact'),
    path('view/', views.view_contact, name='view_contact'),
    path('delete/<int:id>/', views.delete_contact, name='delete_contact'),
]