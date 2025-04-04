import pandas as pd

data_dict = {
    'col_A': [1, 2, 3, 4, 5],
    'col_B': ['P', 'Q', 'R', 'S', 'T'],
    'col_C': [True, False, True, False, True]
}

df = pd.DataFrame(data_dict)

print("DataFrame created from dictionary of lists:")
print(df)