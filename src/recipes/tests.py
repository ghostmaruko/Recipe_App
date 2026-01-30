from django.test import TestCase
from django.utils import timezone
from .models import Recipe
from .forms import RecipeForm

# Lista di 10 ricette vegane per i test
VEGAN_RECIPES = [
    {
        "name": "Vegan Spaghetti Bolognese",
        "description": "Hearty pasta with lentil-tomato sauce",
        "ingredients": "Spaghetti, Lentils, Tomato sauce, Onion, Garlic, Olive oil, Basil",
        "cooking_time": 30,
        "category": "primi",
        "created_at": timezone.now()
    },
    {
        "name": "Chickpea Curry",
        "description": "Spicy chickpea curry with coconut milk",
        "ingredients": "Chickpeas, Onion, Garlic, Ginger, Curry powder, Coconut milk, Spinach",
        "cooking_time": 40,
        "category": "secondi",
        "created_at": timezone.now()
    },
    {
        "name": "Vegan Caesar Salad",
        "description": "Crunchy salad with creamy cashew dressing",
        "ingredients": "Romaine lettuce, Croutons, Cashews, Lemon, Garlic, Nutritional yeast",
        "cooking_time": 15,
        "category": "snack",
        "created_at": timezone.now()
    },
    {
        "name": "Lentil Shepherd's Pie",
        "description": "Savory pie with lentils and mashed potatoes",
        "ingredients": "Lentils, Carrots, Onion, Garlic, Potatoes, Olive oil, Thyme",
        "cooking_time": 50,
        "category": "secondi",
        "created_at": timezone.now()
    },
    {
        "name": "Vegan Pancakes",
        "description": "Fluffy plant-based pancakes",
        "ingredients": "Flour, Almond milk, Baking powder, Maple syrup, Coconut oil",
        "cooking_time": 20,
        "category": "snack",
        "created_at": timezone.now()
    },
    {
        "name": "Tofu Stir-Fry",
        "description": "Quick and colorful vegetable stir-fry",
        "ingredients": "Tofu, Broccoli, Bell peppers, Carrot, Soy sauce, Garlic, Sesame oil",
        "cooking_time": 25,
        "category": "secondi",
        "created_at": timezone.now()
    },
    {
        "name": "Vegan Chocolate Mousse",
        "description": "Creamy chocolate dessert",
        "ingredients": "Avocado, Cocoa powder, Maple syrup, Vanilla extract",
        "cooking_time": 15,
        "category": "dolci",
        "created_at": timezone.now()
    },
    {
        "name": "Quinoa Salad",
        "description": "Protein-packed salad with veggies",
        "ingredients": "Quinoa, Cucumber, Tomato, Bell pepper, Olive oil, Lemon, Parsley",
        "cooking_time": 20,
        "category": "snack",
        "created_at": timezone.now()
    },
    {
        "name": "Veggie Lasagna",
        "description": "Baked pasta with vegetables and tomato sauce",
        "ingredients": "Lasagna sheets, Zucchini, Spinach, Tomato sauce, Vegan cheese",
        "cooking_time": 60,
        "category": "primi",
        "created_at": timezone.now()
    },
    {
        "name": "Coconut Rice Pudding",
        "description": "Sweet coconut dessert",
        "ingredients": "Rice, Coconut milk, Maple syrup, Cinnamon, Vanilla extract",
        "cooking_time": 35,
        "category": "dolci",
        "created_at": timezone.now()
    },
]

class RecipeModelTest(TestCase):
    def setUp(self):
        # Creo tutte le ricette vegane nel DB di test
        for recipe_data in VEGAN_RECIPES:
            Recipe.objects.create(**recipe_data)

    def test_recipe_creation(self):
        """Controlla che tutte le ricette siano state create correttamente"""
        self.assertEqual(Recipe.objects.count(), 10)

    def test_str_method(self):
        """Controlla che il metodo __str__ ritorni il nome della ricetta"""
        for recipe in Recipe.objects.all():
            self.assertEqual(str(recipe), recipe.name)


class RecipeFormTest(TestCase):
    def setUp(self):
        # Dati validi per testare il form
        self.valid_data = {
            "name": "Chickpea Curry",
            "description": "Spicy chickpea curry with coconut milk",
            "ingredients": "Chickpeas, Onion, Garlic, Ginger, Curry powder, Coconut milk, Spinach",
            "cooking_time": 40,
            "category": "secondi",
            "created_at": timezone.now()
        }

    def test_valid_form(self):
        form = RecipeForm(data=self.valid_data)
        print(form.errors)  # debug
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_name(self):
        invalid_data = self.valid_data.copy()
        invalid_data["name"] = ""
        form = RecipeForm(data=invalid_data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_invalid_category(self):
        invalid_data = self.valid_data.copy()
        invalid_data["category"] = "invalid_choice"
        form = RecipeForm(data=invalid_data)
        self.assertFalse(form.is_valid())
