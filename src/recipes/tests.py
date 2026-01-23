from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):
    def setUp(self):
        # Creo una ricetta di esempio
        self.recipe = Recipe.objects.create(
            title="Spaghetti al pomodoro",
            description="Deliziosi spaghetti con salsa di pomodoro fresco.",
            ingredients="Spaghetti, pomodoro, olio, sale, basilico",
            cooking_time=20
        )

    def test_recipe_creation(self):
        # Controlla che la ricetta sia stata creata correttamente
        self.assertEqual(self.recipe.title, "Spaghetti al pomodoro")
        self.assertEqual(self.recipe.cooking_time, 20)

    def test_str_method(self):
        # Controlla che il metodo __str__ ritorni il titolo
        self.assertEqual(str(self.recipe), "Spaghetti al pomodoro")
