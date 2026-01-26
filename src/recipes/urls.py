from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),                     # homepage
    path('all/', views.recipes_list, name='list'),         # lista ricette
    path('all/<int:pk>/', views.recipe_detail, name='detail'),  # dettaglio ricetta
    path('new/', views.recipe_create, name='create'),      # nuova ricetta
    path('all/<int:pk>/edit/', views.recipe_update, name='update'),
    path('all/<int:pk>/delete/', views.recipe_delete, name='delete'),
]
