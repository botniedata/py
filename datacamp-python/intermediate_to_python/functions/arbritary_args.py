# Define a function called concat
def concat(*args):
    """
    Concatenates multiple string arguents with spcaes between them.
    """

    result = ""

    # Iterate over the Python arg tuple
    for arg in args:
        result += " " + arg
    return result

# Call the function
print(concat("Python", "is", "great!"))

