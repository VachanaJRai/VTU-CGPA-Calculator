from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('calculate_sgpa/',views.calculate_sgpa, name='calculate_sgpa'),
    path('calculate_cgpa/',views.calculate_cgpa, name='calculate_cgpa')
]