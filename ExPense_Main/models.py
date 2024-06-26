from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Income(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    source = models.CharField(max_length=9999)
    date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incomes')

    def __str__(self):
        return f"{self.source} - {self.amount}"

COLOR_CHOICES = (
    ('Housing','HOUSING'),
    ('Food', 'FOOD'),
    ('Clothing','CLOTHING'),
    ('Auto','AUTO'),
    ('Insurance','INSURANCE'),
    ('Gym','GYM'),
    ('Loan','LOAN'),
)

class Expense(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=999, choices=COLOR_CHOICES, default='Food')
    date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses', default=None)

class Bill(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    name = models.CharField(max_length=9999, null=True)
    category = models.CharField(max_length=999, choices=COLOR_CHOICES, default='Food')
    date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bills', default=None)
    paid = models.BooleanField(default=False)

Allocation = (
    ('Necessity','NECESSITY'),
    ('Entertainment', 'ENTERTAINMENT'),
    ('Hobby','HOBBY')
)
class Budget(models.Model):
    limit = models.DecimalField(max_digits=6, decimal_places=2)
    nearLimit = models.BooleanField(name="Warning")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    setup = models.BooleanField(default=False)
    
    