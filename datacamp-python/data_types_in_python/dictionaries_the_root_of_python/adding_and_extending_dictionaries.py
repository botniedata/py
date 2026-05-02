# dictionary: squirrels_madison
squirrels_madison = [
 {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Sitting', 'interactions_with_humans': 'Indifferent'},
 {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Cinnamon', 'activities': 'Foraging', 'interactions_with_humans': 'Indifferent'},
 {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Climbing, Foraging', 'interactions_with_humans': 'Indifferent'}]

# tuple: squirrels_union
squirrels_union = ( 'Union Square Park', [
   {'primary_fur_color': 'Gray', 
    'highlights_in_fur_color': None, 
    'activities': 'Eating, Foraging',
    'interactions_with_humans': None}, 
   {'primary_fur_color': 'Gray', 
    'highlights_in_fur_color': 'Cinnamon', 
    'activities': 'Climbing, Eating',
    'interactions_with_humans': None}, 
   {'primary_fur_color': 'Cinnamon', 
    'highlights_in_fur_color': None, 
    'activities': 'Foraging',
    'interactions_with_humans': 'Indifferent'},
   {'primary_fur_color': 'Gray',
    'highlights_in_fur_color': None,
    'activities': 'Running, Digging',
    'interactions_with_humans': 'Runs From'},
   {'primary_fur_color': 'Gray',
    'highlights_in_fur_color': None,
    'activities': 'Digging',
    'interactions_with_humans': 'Indifferent'},
   {'primary_fur_color': 'Gray',
    'highlights_in_fur_color': 'Black',
    'activities': 'Climbing',
    'interactions_with_humans': None},
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Eating, Foraging',
   'interactions_with_humans': None}])

""" Instructions:
1. Assign the 'squirrels_madison' list as the value to the 'Madison Square Park' key of the 'squirrels_by_park' dictionary.
2. Update the 'Union Square Park' key in the 'squirrels_by_park' dictionary with the data in the 'squirrels_union' tuple.
3. Loop over the 'squirrels_by_park' dictionary.
    - Print the 'park_name' and a list of all 'primary_fur_colors' for squirrels safely in that park using a list comprehension; return 'N/A' if the key isn't found.
"""

# dictionary: squirrels_by_park
squirrels_by_park = {'Union Square Park': []}

# Assign squirrels_madision as the value to the 'Madison Square Park' key
squirrels_by_park['Madison Square Park'] = squirrels_madison

# Update squirrels_by_park with the squirrels_union tuple
squirrels_by_park.update([squirrels_union])

# Loop over the park_name in the squirrel_by_park dictionary
for park_name in squirrels_by_park:
    # Safely print a list of the primary_fur_color for each squirrel in park_name
    print(park_name, [squirrel.get('primary_fur_color', 'N/A') for squirrel in squirrels_by_park[park_name]])