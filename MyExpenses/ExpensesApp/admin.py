from django.contrib import admin

# Register your models here.
from ExpensesApp.models import Profile, Expense
admin.site.register(Profile)
admin.site.register(Expense)