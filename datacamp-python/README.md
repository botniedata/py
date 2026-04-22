1. Introduction - Done - 20-April 2026
2. Data Types - Done 20-April 2026
3. Conditional Statements and Operators Done 22-April 2026


### Define quantity
```
quantity = 10
```

### Single quotes
```
ingredient_name = 'pasta'
```

#### Double quotes
```
ingredient_name = "pasta"
```

### Convert to lowercase
```ingredient_name = "Basil Leaves"

ingredient_name = ingredient_name.lower()

# List of ingredients
ingredients = ["pasta", "tomatoes", "garlic", "basil", "olive oil", "salt"]

# Get the value at the first index
ingredients[0]
```

### Create a dictionary
```recipe_dict = {"pasta": 500, "tomatoes": 400, "garlic": 15, "basil": 20, "olive Oil": 30, "salt": 5}
```

### Create a set 
```ingredient_set = {"pasta", "tomatoes", "pasta", "basil", "garlic", "olive oil", "salt"}
```

### Create a  tuple - immitable
```
serving_sizes = (1, 2, 4, 6, 8)
```

### Operator - Function
```== Equal to
!= Not equal to
> More than
>= More than or equal to
< Less than
<= Less than or equal to
```

### Key - Function - Use
```
if - If condition is met - First in the workflow
elif - Else check if condition is met - After if
else - Else perform this action - After elif
```

### For Loop
```
# Ingredients = ["pasta", "tomatoes", "garlic", "basil", "olive oil", "salt"]

# Loop through and print each ingredient
for ingredient in ingredients:
    print(ingredient)

Output:
pasta
tomatoes
garlic
basil
olive oil
salt    
```

### While Loop
```
ingredients_to_add = 5
items_added = 0

while items_added < ingredeints_to_add:
    items_added +=1
    remaining = ingredeints_to_add - items_added

    if remaining > 3:
        print("Several ingredients remaining")
    elif remaining >= 1:
        print("Almost done!")
    else:
        print("Shopping list complete!")
```

### Keywords - Functions
```
and - Evaluate if multiple condition is `true`
or - Evaluate one or more conditions are `true`
in - Evaluate if a value is in a data structure
not - Evaluate if a value is not in a database
```

### .append()
```
list.append()
```