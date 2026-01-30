from django.urls import path
from . import views
from .views import about


app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', about, name='about'),

    path('recipes/', views.recipes_list, name='list'),
    path('recipes/<int:pk>/', views.recipe_detail, name='detail'),

    path('recipes/create/', views.recipe_create, name='create'),
    path('recipes/<int:pk>/edit/', views.recipe_update, name='update'),
    path('recipes/<int:pk>/delete/', views.recipe_delete, name='delete'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('logout/success/', views.logout_success, name='logout_success'),

]
