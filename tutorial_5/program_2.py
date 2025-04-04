import pandas as pd

data = [['Alice', 25, 'New York'],
        ['Bob', 30, 'London'],
        ['Charlie', 35, 'Paris']]

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])

print("Original DataFrame:")
print(df)

df_indexed = df.set_index('Name')

print("\nDataFrame with 'Name' as index:")
print(df_indexed)

custom_index = ['ID1', 'ID2', 'ID3']
df_custom_index = pd.DataFrame(data, columns=['Name', 'Age', 'City'], index=custom_index)
print("\nDataFrame with custom index:")
print(df_custom_index)