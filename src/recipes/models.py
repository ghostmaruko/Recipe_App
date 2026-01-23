from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    cooking_time = models.IntegerField(help_text="Cooking time in minutes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title