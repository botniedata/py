# Dataset dictionary: squirrels
squirrels = [
 ('Marcus Garvey Park', ('Black', 'Cinnamon', 'Cleaning', None)),
 ('Highbridge Park', ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree')),
 ('Madison Square Park', ('Gray', None, 'Foraging', 'Indifferent')),
 ('City Hall Park', ('Gray', 'Cinnamon', 'Eating', 'Approaches')),
 ('J. Hood Wright Park', ('Gray', 'White', 'Running', 'Indifferent')),
 ('Seward Park', ('Gray', 'Cinnamon', 'Eating', 'Indifferent')),
 ('Union Square Park', ('Gray', 'Black', 'Climbing', None)),
 ('Tompkins Square Park', ('Gray', 'Gray', 'Lounging', 'Approaches'))]

""" Instruction:
1. Create an empty dictionary called 'squirrels_by_park.'
2. Loop over 'squirrels', unpacking it into the variables 'park' and 'squirrel_details'.
3. Inside the loop, add each 'squirrel_details' to the 'squirrels_by_park' dictionary using the 'park'as the key.
4. Sort the 'squirrel_details' dictionary keys in ascending order, print each park and its value using an F string..
"""

# Create an empty dictionary: squirrels_by_park
squirrels_by_park = {}

# Loop over the squirrels list and unpack each tuple
for park, squirrel_details in squirrels:
    # Add each squirrel_details to the squirrels_by_park dictionary
    squirrels_by_park[park] = squirrel_details 

# Sort the squirrels_by_park dict alphabetically by park
for park in sorted(squirrels_by_park):
    # Print each park its value in squirrels_by_park
    print(f'{park}: {squirrels_by_park[park]}')