from django.shortcuts import render, redirect
from expenses.models import Expense  # Assuming you have a model named Expense

def home(request):
    # You can either render a home page template or redirect to the expense list
    return redirect('expense_list')  # Redirects to the expense list page
