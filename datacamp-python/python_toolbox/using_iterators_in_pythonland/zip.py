mutants = ['charles xavier',
           'bobby drake',
           'kurt wagner',
           'max eisenhardt',
           'kitty pryde']

aliases = [('cat', 'cat'),
           ('cp', 'cp'),
           ('ldir', 'ls -F -o %l | grep /$'),
           ('lf', 'ls -F -o %l | grep ^-'),
           ('lk', 'ls -F -o %l | grep ^l'),
           ('ll', 'ls -F -o'),
           ('ls', 'ls -F'),
           ('lx', 'ls -F -o %l | grep ^-..x'),
           ('mkdir', 'mkdir'),
           ('mv', 'mv'),
           ('rm', 'rm'),
           ('rmdir', 'rmdir')]

powers = ['telepathy',
          'thermokinesis',
          'teleportation',
          'magnetokinesis',
          'intangibility']


# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for  value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)