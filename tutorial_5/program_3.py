import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

excel_filename = 'output_data.xlsx'

df.to_excel(excel_filename, index=False, sheet_name='Sheet1')

print(f"Data successfully written to {excel_filename}")