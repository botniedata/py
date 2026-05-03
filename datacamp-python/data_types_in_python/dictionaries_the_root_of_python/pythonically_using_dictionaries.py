# Loaded dictionaries
squirrels_by_park = {
   'Madison Square Park': [
   {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Foraging',
   'interactions_with_humans': 'Indifferent'},
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Sitting',
   'interactions_with_humans': 'Indifferent'}],
 'Union Square Park': [{'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Eating, Foraging',
   'interactions_with_humans': None},
  {'primary_fur_color': 'Cinnamon',
   'highlights_in_fur_color': None,
   'activities': 'Foraging',
   'interactions_with_humans': None},
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Eating, Foraging',
   'interactions_with_humans': None},
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Digging',
   'interactions_with_humans': 'Indifferent'}] }

""" Instructions:
1. Iterate over the first record in squirrels_by_park["Madison Square Park"], unpacking its items into field and value.
    - Print each field and value.
2. Repeat the process for the second record in squirrels_by_park["Union Square Park"].
"""


# Iterate over the first squirrel entry in the Madison Square Park List
for field, value, in squirrels_by_park['Madison Square Park'][0].items():
    # Print field and value
    print(field, value)

print('-' * 13)

# Iterate over the second squirrel entry in the Union Square Park list
for field, value in squirrels_by_park['Union Square Park'][1].items():
    # Print field and value
    print(field, value)