from django.contrib import admin
from .models import Income, Expense, Budget, Bill, UserProfile
# Register your models here.
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Budget)
admin.site.register(Bill)
admin.site.register(UserProfile)