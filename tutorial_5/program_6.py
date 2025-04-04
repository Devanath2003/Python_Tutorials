import pandas as pd
import io

data_string = """SN,Name,Country,Contribution,Year
1,Linus Torvalds,Finland,Linux Kernel,1991
2,Tim Berners-Lee,England,World Wide Web,1990
3,Guido van Rossum,Netherlands,Python,1991
"""

data_io = io.StringIO(data_string)

df = pd.read_csv(data_io)

csv_filename = 'contributors.csv'

df.to_csv(csv_filename, index=False)

print(f"Data successfully written to {csv_filename}")
print("\nDataFrame content:")
print(df)