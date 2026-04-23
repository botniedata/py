# Import os and string module
import os
import string

user_password = 'SecurePass123'

def validate_password(password):
    # Check if password is at least 8 characters long
    if len(password) >= 8:
        # Check if passsword contains a special character
        for char in password:
            if char in string.punctuation:
                return True
    return False


# Call the function and store the result
is_valid = print(validate_password(user_password))
print("Is the password valid? ", is_valid)