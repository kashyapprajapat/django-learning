from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm  # You will create this form in the next step

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

def expense_add(request):
    print("Accessing expense_add view")
    print("Rendering template: expense_form.html")
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_form.html', {'form': form})


def expense_edit(request, pk):
    expense = Expense.objects.get(id=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/expense_form.html', {'form': form})

def expense_delete(request, pk):
    expense = Expense.objects.get(id=pk)
    expense.delete()
    return redirect('expense_list')
