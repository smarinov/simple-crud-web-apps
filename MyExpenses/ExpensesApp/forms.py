from django import forms

from ExpensesApp.models import Profile, Expense


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = '__all__'
        exclude = ('profile',)


