# Lists of feature_names and row_vals
feature_names = ['CountryName',
                 'CountryCode',
                 'IndicatorName',
                 'IndicatorCode',
                 'Year',
                 'Value']

row_vals = ['Arab World',
            'ARB',
            'Adolescent fertility rate (births per 1,000 women ages 15-19)',
            'SP.ADO.TFRT',
            '1960',
            '133.56090740552298']

# Zip list:s: zipped_list
zipped_list = zip(feature_names, row_vals)

# Create a dictionary: rs_dict
rs_dict = dict(zipped_list)

# Print the dictionary
print(rs_dict)