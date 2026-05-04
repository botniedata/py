# Load dataset: weight_log
weight_log = [('Chinstrap', 'FEMALE', 3800.0),
 ('Adlie', 'FEMALE', 3450.0),
 ('Gentoo', 'FEMALE', 4300.0),
 ('Adlie', 'FEMALE', 3550.0),
 ('Adlie', 'FEMALE', 3175.0)]

""" Instructions: 
1. Create an empty dictionary called female_penguin_weights.
2. Iterate over weight_log, unpacking it into the variables species, sex, and body_mass.
3. Check to see if the species already exists in the female_penguin_weights dictionary. If it does not exist, create an empty list for the species key. Then, append a tuple consisting of sex and body_mass to the species key of the female_penguin_weights dictionary for all entries in the weight_log.
4. Print the female_penguin_weights for 'Adlie'

"""

# Create an empty dictionaries called 
female_penguin_weights = {}

# Iterate over the weight_log entries
for species, sex, body_mass in weight_log:
    # Check to see if species is already in the dictionary
    if species not in female_penguin_weights:
        # Create an empty list for any missing species
        female_penguin_weights[species] = []
    # Append the sex and body_mass as an tuple to the species keys list
    female_penguin_weights[species].append((sex, body_mass))

# Print the weights for 'Adlie'
print(female_penguin_weights['Adlie'])

