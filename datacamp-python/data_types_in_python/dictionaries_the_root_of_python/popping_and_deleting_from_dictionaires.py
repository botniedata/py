squirrels_by_park = {'Madison Square Park': [{'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Foraging',
   'interactions_with_humans': 'Indifferent'},
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Sitting',
   'interactions_with_humans': 'Indifferent'}],
 'Tompkins Square Park': [{'primary_fur_color': 'Gray',
   'highlights_in_fur_color': 'Gray',
   'activities': 'Foraging',
   'interactions_with_humans': 'Approaches'},
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': 'Gray',
   'activities': 'Climbing (down tree)',
   'interactions_with_humans': 'Indifferent'},
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': 'Gray',
   'activities': 'Foraging',
   'interactions_with_humans': 'Indifferent'},
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': 'Gray',
   'activities': 'Foraging',
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
   'interactions_with_humans': 'Indifferent'}]}

""" Instructions:
1. Remove "Madison Square Park" from 'squirrels_by_park' and store it as 'squirrels_madison'.
2. Safely remove "City Hall Park" from 'squirrels_by_park' with a empty dictionary as the default and store it as 'squirrels_city_hall'. To do this, pass in an empty dictionary '{}' as a second argument to '.pop()'.
3. Delete "Union Square Park" from 'squirrels_by_park'.
4. Print 'squirrels_by_park'.
"""

# Remove  "Madison Square Park" from squirrels_by_park
squirrels_madison = squirrels_by_park.pop('Madison Square Park')

# Safely remove "City Hall Park" from squirrels_by_oa
squirrels_city_hall = squirrels_by_park.pop('City Square Park', {})

# Delete "Union Square Park" from squirrel_by_park
del squirrels_by_park['Union Square Park']

# Print squirrels_by_park
print(squirrels_by_park)