from django.shortcuts import render, redirect

# Create your views here.
from app.forms import RecipeForm, DeleteRecipe
from app.models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }

    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'GET':
        form = RecipeForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'create.html', {'form': form})


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        form = RecipeForm(instance=recipe)
        context = {
            'recipe': recipe,
            'form': form,
        }
        return render(request, 'edit.html', context)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form,
        }
        return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        form = DeleteRecipe(instance=recipe)
        context = {
            'recipe': recipe,
            'form': form,
        }
        return render(request, 'delete.html', context)
    else:
        recipe.delete()
        return redirect('index')


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }

    return render(request, 'details.html', context)
