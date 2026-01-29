from django.db import models
from django.urls import reverse
from django.utils import timezone 

class Recipe(models.Model):

    CATEGORY_CHOICES = [
        ('antipasti', 'Antipasti'),
        ('primi', 'Primi'),
        ('secondi', 'Secondi'),
        ('contorni', 'Contorni'),
        ('dolci', 'Dolci'),
    ]

    name = models.CharField(max_length=120)
    description = models.TextField()
    ingredients = models.TextField()
    cooking_time = models.PositiveIntegerField(help_text="In minutes")
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        blank=True
    )
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return self.name

    def calculate_difficulty(self):
        if self.cooking_time < 10:
            return "Easy"
        elif self.cooking_time < 30:
            return "Medium"
        return "Hard"

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})
