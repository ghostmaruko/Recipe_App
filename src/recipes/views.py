from django.shortcuts import render, get_object_or_404, redirect

from recipes.forms import RecipeForm
from .models import Recipe
from .forms import RecipeForm


# Lista ricette (overview)
def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipes_list.html', {'recipes': recipes})

# Dettaglio ricetta
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

# Create new recipe
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes:list')  # dopo il salvataggio torna alla lista
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

# Update recipe
def recipe_update(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes:detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form})

# Delete recipe
def recipe_delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes:list')
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})

def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes:list')  # dopo il salvataggio, torna alla lista
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

def home(request):
    return render(request, 'recipes/welcome.html')
