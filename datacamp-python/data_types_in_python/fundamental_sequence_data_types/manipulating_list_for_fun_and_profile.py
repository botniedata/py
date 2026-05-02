# Create a list containing the names: baby_names
baby_names = ['Ximena', 'Aliza', 'Ayden', 'Calvin']

# Extend baby_names with 'Rowen' and 'Sandeep'
baby_names.extend(['Rowen', 'Sandeep'])
print(baby_names)

# Find the position of 'Rowen': position
position = baby_names.index('Rowen')
print(position)

# Remove 'Rowen' from baby_names
baby_names.pop(4) # index position as arguement

# Print baby_names
print(baby_names)