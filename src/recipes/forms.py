from django import forms
from .models import Recipe

# Form per creare o modificare le ricette
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "ingredients": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "cooking_time": forms.NumberInput(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

# Form per la ricerca delle ricette
CATEGORY_CHOICES = [
    ('', 'All'),
    ('antipasti', 'Antipasti'),
    ('primi', 'Primi'),
    ('secondi', 'Secondi'),
    ('contorni', 'Contorni'),
    ('dolci', 'Dolci'),
]

class RecipeSearchForm(forms.Form):
    recipe_name = forms.CharField(
        required=False,
        label="Recipe name",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )

    category = forms.ChoiceField(
        required=False,
        choices=[("", "All categories")] + Recipe.CATEGORY_CHOICES,
        label="Category"
    )