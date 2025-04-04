import pandas as pd

data = {'Product': ['Apple', 'Banana', 'Orange'],
        'Price': [1.2, 0.5, 0.8],
        'Quantity': [100, 150, 200]}
df = pd.DataFrame(data)

excel_filename = 'product_data.xlsx'

df.to_excel(excel_filename, index=False, sheet_name='Products')

print(f"Data successfully written to {excel_filename}")