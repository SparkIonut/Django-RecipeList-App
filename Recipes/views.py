from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Recipe
from .forms import RecipeForm

def recipe_list(request):
    recipes = Recipe.objects.filter(Recipe_Date__lte=timezone.now()).order_by('Recipe_Date')
    return render(request, 'Recipes/MainPage.html', {'recipes': recipes})

def recipe_details(request, recipe_title):
    recipe = get_object_or_404(Recipe, pk=recipe_title)
    return render(request, 'Recipes/recipe_details.html', {'recipe': recipe})

def recipe_add(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.Recipe_Owner = request.user
            recipe.Recipe_Date = timezone.now()
            recipe.save()
            return redirect('recipe_details', recipe_title=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'Recipes/recipe_add.html', {'form': form})

def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.Recipe_Owner = request.user
            recipe.Recipe_Date = timezone.now()
            recipe.save()
            return redirect('recipe_details', recipe_title=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'Recipes/recipe_edit.html', {'form': form,})

def test_hero(request):
    return render(request, 'Hero/blog-simple.html')