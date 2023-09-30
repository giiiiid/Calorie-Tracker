from django.urls import path
from . import views

urlpatterns=[
    path('home/', views.home, name='home'),
    path('delete/<str:id>', views.delete, name='delete'),
]