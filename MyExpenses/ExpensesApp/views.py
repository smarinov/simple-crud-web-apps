from django.shortcuts import render, redirect

# Create your views here.
from ExpensesApp.forms import ExpenseForm, ProfileForm
from ExpensesApp.models import Profile, Expense


def home(request):
    profile = Profile.objects.first()
    if not profile:
        if request.method == 'GET':
            form = ProfileForm()
            return render(request, 'home-no-profile.html', {'form': form})
        else:
            expenses = Expense.objects.all()
            form = ProfileForm(request.POST)
            form.save()
            return render(request, 'home-with-profile.html', {'expenses': expenses})
    else:
        expenses = Expense.objects.all()
        total_expense = profile.budget - sum([x.price for x in Expense.objects.all()])
        context = {
            'expenses': expenses,
            'total_expense': total_expense,
            'profile': profile,
        }
        return render(request, 'home-with-profile.html', context)


def create(request):
    if request.method == "GET":
        form = ExpenseForm()
        return render(request, 'expense-create.html', {'form': form})
    else:
        profile = Profile.objects.first()
        form = ExpenseForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.profile = profile
            test.save()
            return redirect('homepage')
        return render(request, 'expense-create.html', {'form': form})


def edit(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == "GET":
        form = ExpenseForm(instance=expense)
        return render(request, 'expense-edit.html', {'form': form})
    else:
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            return render(request, 'expense-edit.html', {'form': form})


def delete(request, pk):
    expense = Expense.objects.get(pk=pk)
    form = ExpenseForm(instance=expense)
    if request.method == "GET":
        return render(request, 'expense-delete.html', {'form': form})
    else:
        expense.delete()
        return redirect('homepage')


def profile(request):
    prof = Profile.objects.first()
    total_expense = prof.budget - sum([x.price for x in Expense.objects.all()])
    return render(request, 'profile.html', {'prof': prof, 'budget_left': total_expense})


def edit_profile(request):
    form = ProfileForm(instance=Profile.objects.first())
    if request.method == "GET":
        return render(request, 'profile-edit.html', {'form': form})
    else:
        form = ProfileForm(request.POST, instance=Profile.objects.first())
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return render(request, 'profile-edit.html', {'form': form})


def delete_profile(request):
    prof = Profile.objects.first()
    if request.method == 'GET':
        return render(request, 'profile-delete.html', {'prof': prof})
    else:
        prof.delete()
        return redirect('homepage')
