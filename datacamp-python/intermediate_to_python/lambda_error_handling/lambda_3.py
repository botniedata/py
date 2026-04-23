colleagues = ["Sarah Martinez", "Michael Chen", "Emily Brown"]

# Apply the lambda function to each colleague's
cleaned = map(lambda x : x.replace(" ", "_").lower(), colleagues)

# Convert map objject to list
cleaned_list = list(cleaned)
print(cleaned_list)