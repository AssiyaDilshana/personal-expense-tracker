from django.db import models
from django.contrib.auth.models import User

# Category model (Food, Travel, Rent, etc.)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Transaction model
class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} - {self.amount} ({self.category.name})"
