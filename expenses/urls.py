from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),  # Make sure the list is the root of this app
    path('add/', views.expense_add, name='expense_add'),
    path('edit/<int:pk>/', views.expense_edit, name='expense_edit'),
    path('delete/<int:pk>/', views.expense_delete, name='expense_delete'),
]
