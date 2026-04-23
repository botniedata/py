full_name = "Alan Turing"

# Define the generate_email function
def generate_email(full_name):
    # Split the full_name
    name_parts = full_name.split()
    # Change the name_part into lowercase and concatinate 
    email = name_parts[0].lower() + '.' + name_parts[1].lower() + '@techcompany.com'

    # Return the email address
    return email

# Call the function on the full_name string
print(generate_email(full_name))