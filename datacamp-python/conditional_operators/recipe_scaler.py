# Recipe dictionary with key-value pairs: ingredient:amount
recipe = {
    'pasta': 500,
    'tomatoes': 400,
    'garlic': 15,
    'basil': 20,
    'olive_oil': 30,
    'salt': 10}

# Pantry dictionary
pantry = {
    'pasta': 500, 
    'tomatoes': 800, 
    'olive_oil': 100, 
    'garlic': 15
    }

scale_factor = 2.5

# Empty container of shopping list to iterate
shopping_list = []

# Loop through each ingredient and amount in the recipe
for ingredient, amount in recipe.items():
    # Calculate the needed_amount by multiplying the amount by the scale_factor
    needed_amount = amount * scale_factor

    # Check if we need to by this ingredient
    '''
    Check if the 'ingredient' IS NOT in 'pantry' OR if the 'needed_amount' is greater than the quantity in 'pantry[ingredient]'. If either is true, append the 'ingredient' to 'shopping_list'.
    '''
    if ingredient not in pantry or needed_amount > pantry[ingredient]:
        shopping_list.append(ingredient)

print("Shopping list for your party:")
print(shopping_list)