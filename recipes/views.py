# recipes/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Recipe, Comment, Like
from .forms import RecipeForm, CommentForm

def recipe_list(request):
    recipes = Recipe.objects.all().order_by('-created_at')
    form = RecipeForm()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                recipe = form.save(commit=False)
                recipe.author = request.user
                recipe.save()
                messages.success(request, 'Your recipe has been added.')
                return redirect('recipes:recipe_list')
        else:
            return redirect('users:login')
    context = {
        'recipes': recipes,
        'form': form,
    }
    return render(request, 'recipes/recipe_list.html', context)

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    comments = recipe.comments.order_by('-created_at')
    comment_form = CommentForm()
    user_liked = False
    if request.user.is_authenticated:
        user_liked = recipe.likes.filter(user=request.user).exists()
    context = {
        'object': recipe,
        'comments': comments,
        'comment_form': comment_form,
        'user_liked': user_liked,
    }
    return render(request, 'recipes/recipe_detail.html', context)

@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, 'Your recipe has been created.')
            return redirect('recipes:recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

@login_required
def add_comment(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been added.')
            return redirect('recipes:recipe_detail', pk=recipe.pk)
    else:
        form = CommentForm()
    return render(request, 'recipes/add_comment.html', {'form': form})

@login_required
def like_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    like, created = Like.objects.get_or_create(recipe=recipe, user=request.user)
    if not created:
        # User already liked this recipe, so unlike
        like.delete()
        messages.info(request, 'You have unliked this recipe.')
    else:
        messages.success(request, 'You have liked this recipe.')
    return redirect('recipes:recipe_detail', pk=pk)
