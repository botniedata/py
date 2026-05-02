doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']

range(50)

underwood = 'After all, we are nothing more or less than what we choose to reveal.'

jean = '24601'

flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

valjean = 24601

# List comprehension #1
one = [doc[2::] for doc in doctor]
print(one)

# List comprehension #2
two = [x[-1] for x in underwood]
print(two)

# List comprehension #3
three = [y+ str(1) for y in jean]
print(three)

# List comprehension #4
four = [z[1] for z in flash]
print(four)

# List comprehension #5 - can build list comprehension over all the objects except the integer object 'valjean'
five = [a+1 for a in valjean]
print(five)
