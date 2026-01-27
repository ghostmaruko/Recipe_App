from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Recipe
from .forms import RecipeForm

# Homepage
def home(request):
    return render(request, 'recipes/welcome.html')


# Lista ricette (overview) - protetta
@login_required
def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipes_list.html', {'recipes': recipes})


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
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)  # <-- aggiunto request.FILES
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
    return redirect('recipes:logout_success')  # namespace corretto!


# Logout success page
def logout_success(request):
    return render(request, 'auth/success.html')
