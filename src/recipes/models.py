from django.db import models
from django.urls import reverse

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    ingredients = models.TextField()
    cooking_time = models.PositiveIntegerField(help_text="in minutes")
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)

    def __str__(self):
        return self.name

    def calculate_difficulty(self):
        if self.cooking_time < 10:
            return "Easy"
        elif self.cooking_time < 30:
            return "Medium"
        else:
            return "Hard"

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})
