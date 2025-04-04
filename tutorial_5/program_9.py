import pandas as pd
import io

csv_filename = 'contributors.csv'

try:
    pd.read_csv(csv_filename)
except FileNotFoundError:
    print(f"File {csv_filename} not found. Creating a dummy file first.")
    data_string = """SN,Name,Country,Contribution,Year
1,Linus Torvalds,Finland,Linux Kernel,1991
2,Tim Berners-Lee,England,World Wide Web,1990
3,Guido van Rossum,Netherlands,Python,1991
"""
    data_io = io.StringIO(data_string)
    df_write = pd.read_csv(data_io)
    df_write.to_csv(csv_filename, index=False)
    print(f"Dummy file {csv_filename} created.")

try:
    df = pd.read_csv(csv_filename)

    print(f"Reading data from {csv_filename}")
    print("\nFirst 5 records:")
    print(df.head(5))

except FileNotFoundError:
    print(f"Error: Could not find {csv_filename} to read.")