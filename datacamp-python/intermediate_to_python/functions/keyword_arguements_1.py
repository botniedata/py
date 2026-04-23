# Defined product name
product = 'Wireless Mouse'

'''
    Define clean_text function with parameters 'text' and 'lower' with default value of 'True'
'''
def clean_text(text , lower=True ):
    clean_text = text.replace(' ', '-')
    if lower == False:
        return clean_text
    # Inside the else block, apply the lowercase transformation
    else:
        # Apply lowercase transformation
        return clean_text.lower()

'''
Call the function 'clean_text() with 'product' as the arguement to test the default behavior
'''
print(clean_text(product))

