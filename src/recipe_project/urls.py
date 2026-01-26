from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # HOMEPAGE → recipes.home
    path('', include('recipes.urls')),

    # lista ricette → /all/
    path('all/', include('recipes.urls')),
]
