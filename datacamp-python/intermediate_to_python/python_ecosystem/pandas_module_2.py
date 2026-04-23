sales = {
    'user_id': 
    [
        'KM37', 'PR19', 'YU88', 'JB18', 'LP65', 'HJ11', 'PR19', 'IJ54'
    ],
    'date': 
    [
        '01/05/2025', 
        '01/05/2025', 
        '01/06/2025', 
        '01/06/2025',
        '01/06/2025',
        '01/06/2025',
        '01/07/2025',
        '01/07/2025'
    ],
    'order_value': 
    [
        197.75, 208.21, 134.99, 317.81, 201.3, 157.87, 99.99, 124.5
    ]
        }


# Import pandas as pd
import pandas as pd

# Convert sales to pandas DataFrame
sales_df = pd.DataFrame(sales)

# Preview the first few rows
print(sales_df.head())