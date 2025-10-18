from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['description', 'amount', 'transaction_type', 'category', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'}),
            'transaction_type': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category'}),
        }
