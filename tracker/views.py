from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Transaction
from .forms import TransactionForm

# --------------------------
# Dashboard (after login)
# --------------------------
@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    income = sum(t.amount for t in transactions if t.transaction_type == 'Income')
    expense = sum(t.amount for t in transactions if t.transaction_type == 'Expense')
    balance = income - expense

    return render(request, 'tracker/dashboard.html', {
        'transactions': transactions,
        'income': income,
        'expense': expense,
        'balance': balance,
    })

# --------------------------
# Add Transaction
# --------------------------
@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'tracker/add_transaction.html', {'form': form})

# --------------------------
# Register (Sign Up)
# --------------------------
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # auto-login after registration
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})
