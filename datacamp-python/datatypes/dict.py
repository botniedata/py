# Dictionary = key-value pairs

# Create the recipe dictionary
recipe = {
    "olive_oil": 30,
    "garlic":15,
    "tomatoes": 400
}

# Add basil to the recipe dictionary
recipe["basil"] = 20
print(recipe)

# Get all ingredient names
ingredient_names = recipe.keys()

# Get all quantities
quantities = recipe.values()

# Get all key-value pairs as tuples
recipe_items = recipe.items()

print("Ingredient names:", ingredient_names)
print("Quantities:", quantities)
print("Recipe items:", recipe_items)