original_price = 899.99

'''
Define the 'calculate_discount() function with default arguments for 'discount_percent' (15) and 'round_result' (True)
'''
def calculated_discount(price, discount_percent = 15, round_result = True):
    discounted_price = price - (price * discount_percent / 100)

    if round_result == True:
        # Round the result to two decimal places
        return round(discounted_price, 2)
    else:
        return discounted_price
    
# Call the function with keyword arguements
final_price = calculated_discount(price = original_price, discount_percent = 25, round_result = False)
print(final_price)