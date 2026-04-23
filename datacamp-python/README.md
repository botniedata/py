## Introduction to Python for Developers

### Define quantity
```
quantity = 10
```

### Single quotes
```
ingredient_name = 'pasta'
```

### Double quotes
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
```
recipe_dict = {"pasta": 500, "tomatoes": 400, "garlic": 15, "basil": 20, "olive Oil": 30, "salt": 5}
```

### Create a set 
```
ingredient_set = {"pasta", "tomatoes", "pasta", "basil", "garlic", "olive oil", "salt"}
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

## Intermediate to Python for Developers
### Python Ecosystem
### Built-in functions
`print()`, `help()`, `type()`
`max()`, `min()`, `sum()`
`len()`, `round()`, `sorted()`

### Modules
`string`, `os`

### Packages
`pandas`

#### Customs Function
```
# Create a custom function
def average(values):
    # Calculate the average
    average_value = sum(values) / len(values)

    # Round the result
    rounded_average = round(average_values, 2)

    # Return rounded_average as an output
    return rounded_average
```

### Enhanced Custom Function with default arguements
```
# Create a custom function
def average(values, rounded=False):
    # Round average to two decimal places if rounded is True
    if rounded == True:
        average_value = sum(values) / len(values)
        rounded_average = round(average_value, 2)
        return rounded_average
    # Otherwise, don't round
    else:
        average_value = sum(values) / len(values)
        return average_value
```

### Docstrings
```
def average(values):
    """
    Fine the mean in a sequence of values and round to two decimal places.

    Args:
        values (list): A lit of numeric values

    Returns:
        rounded_average (float): The mean of values, rounded to two decimal places
    """

average_values = sum(values) / len(values)
rounded_average = round(average_value, 2)
return rounded_average
```

### Arbritrary Positional and Arbritrary Keyword Arguements
```
# Use arbritrary positional arguements
def average(*args):
    average_value = sum(args) / len(args)
    rounded_average = round(average_value, 2)
    return rounded_average

# Use arbritary keyword arguements
def average(**kwargs):
    average_value = sum(kwargs.values()) / len(kwargs.values())
    rounded_average = round(average_value, 2)
    return rounded_average
```
