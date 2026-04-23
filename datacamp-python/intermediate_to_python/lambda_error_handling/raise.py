def clean_text(text):
    # Check the data type
    if type(text) == str:
        return text.replace(" ", "_").lower()
    else:
        # Return a TypeError if the wrong data type was used
        raise TypeError("The clean _text() function expects a string as arguement, please check the data type provieded!")

print(clean_text("User Name 187"))