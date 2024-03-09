# Inside recipes/views.py
import json
from django.shortcuts import render
from django.conf import settings
from os.path import join

def recipe_list(request):
    # Path to your JSON file
    json_path = join(settings.BASE_DIR, 'recipes/static/recipes/italian_appetizer_recipes.json')
    # Load the JSON data
    with open(json_path) as file:
        recipes = json.load(file)  # Directly load the list of recipes
    selected_recipe = None
    if request.method == 'POST':
        selected_recipe_name = request.POST.get('recipe')
        for recipe in recipes:  # Iterate directly over the list
            if recipe['name'] == selected_recipe_name:
                selected_recipe = recipe
                break

    # Pass the recipes data and the selected recipe (if any) to the template
    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'selected_recipe': selected_recipe
    })
