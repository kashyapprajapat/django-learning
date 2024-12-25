from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Expense Title'}),
            'amount': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Amount'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }
