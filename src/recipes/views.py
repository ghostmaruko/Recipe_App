from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Count
import os

from .models import Recipe
from .forms import RecipeForm, RecipeSearchForm

import pandas as pd
import matplotlib.pyplot as plt

# Homepage
def home(request):
    return render(request, 'recipes/welcome.html')


# Lista ricette (overview) - protetta
@login_required
def recipes_list(request):
    form = RecipeSearchForm(request.GET or None)
    recipes = Recipe.objects.all()

    if form.is_valid():
        name = form.cleaned_data.get("recipe_name")
        category = form.cleaned_data.get("category")

        if name:
            recipes = recipes.filter(name__icontains=name)
        if category:
            recipes = recipes.filter(category=category)

    # ===== PANDAS TABLE =====
    recipes_qs = recipes.values("id", "name", "cooking_time")
    df = pd.DataFrame.from_records(recipes_qs)

    if not df.empty:
        # rendiamo il nome cliccabile
        df["name"] = df.apply(
            lambda row: f'<a href="{reverse("recipes:detail", args=[row["id"]])}">{row["name"]}</a>',
            axis=1
        )

    table = df.to_html(
        classes="table table-striped table-hover",
        index=False,
        escape=False
    )

    # ===== BAR CHART =====
    category_counts = recipes.values("category").annotate(count=Count("id"))
    df_cat = pd.DataFrame.from_records(category_counts)

    if not df_cat.empty:
        # percorso static sicuro
        static_dir = os.path.join(os.path.dirname(__file__), 'static', 'recipes')
        os.makedirs(static_dir, exist_ok=True)
        chart_path = os.path.join(static_dir, 'category_bar.png')

        plt.figure()
        plt.bar(df_cat["category"], df_cat["count"])
        plt.xlabel("Category")
        plt.ylabel("Number of Recipes")
        plt.title("Recipes per Category")
        plt.tight_layout()
        plt.savefig(chart_path)
        plt.close()

    context = {
        "form": form,
        "recipes": recipes,
        "table": table,
    }

    return render(request, "recipes/recipes_list.html", context)


# Dettaglio ricetta - protetta
@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


# Create new recipe - protetta
@login_required
def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes:list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})


# Update recipe - protetta
@login_required
def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes:detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form})


# Delete recipe - protetta
@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes:list')
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})


# Login view
def login_view(request):
    error_message = None
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recipes:list')
        else:
            error_message = 'Invalid username or password'

    return render(request, 'auth/login.html', {
        'form': form,
        'error_message': error_message
    })


# Logout view
def logout_view(request):
    logout(request)
    return redirect('recipes:logout_success')


# Logout success page
def logout_success(request):
    return render(request, 'auth/success.html')


# Recipe search view (opzionale)
@login_required
def recipe_search(request):
    form = RecipeSearchForm(request.GET or None)
    recipes = Recipe.objects.all()

    if form.is_valid():
        name = form.cleaned_data.get('recipe_name')
        category = form.cleaned_data.get('category')

        if name:
            recipes = recipes.filter(name__icontains=name)
        if category:
            recipes = recipes.filter(category=category)

    context = {
        'form': form,
        'recipes': recipes
    }

    return render(request, 'recipes/search.html', context)
