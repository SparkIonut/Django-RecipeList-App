from django import forms

from .models import Recipe

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('Recipe_Title', 'Recipe_Tags', 'Recipe_Ingredients', 'Recipe_Description')