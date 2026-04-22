# key-value pairs of ingredient and required_qty in recipe
recipe = {
    'pasta': 500,
    'tomatoes': 400,
    'basil': 20,
    'garlic': 15,
    'olive_oil': 30,
    'salt': 10
}

# key-value pairs of ingredient and required_qty in pantry_stock
pantry_stock = {
    'pasta': 100,
    'tomatoes': 1500,
    'basil': 20,
    'garlic': 10,
    'olive_oil': 10,
    'salt': 150}

# Create an empty shopping list
shopping_list = []

# Loop through each ingredient and required quantity
for ingredient, required_qty in recipe.items():
    # Chech if we need more than what we have
    if required_qty > pantry_stock[ingredient]:
        # Add the ingredient to our shopping list
        shopping_list.append(ingredient)

# Display thhe shopping list
print("Shopping list:", shopping_list)

# Count how many items to buy
items_to_buy = 0

# Create a loop increate 1 for each ingredient in shopping_list
for item in shopping_list:
    items_to_buy +=1

# Display the shopping_list and total number of items_to_buy
print("List of items to by", shopping_list, "with the total number of", items_to_buy, "items")