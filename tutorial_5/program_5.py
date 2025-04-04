import pandas as pd

excel_filename = 'output_data.xlsx'

try:
    df_read = pd.read_excel(excel_filename)
    print(f"Successfully read data from {excel_filename}:")
    print(df_read)
except FileNotFoundError:
    print(f"File {excel_filename} not found. Creating a dummy file first.")
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'London', 'Paris']}
    df_write = pd.DataFrame(data)
    df_write.to_excel(excel_filename, index=False, sheet_name='Sheet1')
    print(f"Dummy file {excel_filename} created.")
    df_read = pd.read_excel(excel_filename)
    print(f"\nSuccessfully read data from newly created {excel_filename}:")
    print(df_read)

try:
    df_read = pd.read_excel(excel_filename)
    print(f"\nReading {excel_filename} again:")
    print(df_read)
except FileNotFoundError:
     print(f"Error: Could not find {excel_filename} to read.")