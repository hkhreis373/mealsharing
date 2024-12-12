from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/new/', views.recipe_create, name='recipe_create'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('recipe/<int:pk>/like/', views.like_recipe, name='like_recipe'),
]
