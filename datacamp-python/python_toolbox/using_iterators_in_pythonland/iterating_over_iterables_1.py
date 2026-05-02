# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for person in flash:
    print(person)

# Create a iterator for flash: superhero
superhero = iter(flash)

# Print each item for the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))