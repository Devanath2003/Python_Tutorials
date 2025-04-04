import pandas as pd
import io

csv_data = """index,company,body-style,wheel-base,length,engine-type,num-of-cylinders,horsepower,average-mileage,price
0,alfa-romero,convertible,88.6,168.8,dohc,four,111,21,13495
1,alfa-romero,convertible,88.6,168.8,dohc,four,111,21,16500
2,alfa-romero,hatchback,94.5,171.2,ohcv,six,154,19,16500
3,audi,sedan,99.8,176.6,ohc,four,102,24,13950
4,audi,sedan,99.4,176.6,ohc,five,115,18,17450
5,audi,sedan,99.8,177.3,ohc,five,110,19,15250
"""
csv_filename = "auto.csv"
with open(csv_filename, 'w') as f:
    f.write(csv_data)
print(f"Dummy file '{csv_filename}' created for demonstration.")

try:
    df_auto = pd.read_csv(csv_filename)

    df_auto_cleaned = df_auto.copy()
    print("\n1) Cleaned DataFrame head:")
    print(df_auto_cleaned.head())

    most_expensive_car = df_auto_cleaned.loc[df_auto_cleaned['price'].idxmax()]
    most_expensive_company = most_expensive_car['company']
    print(f"\n2) Most expensive car company: {most_expensive_company}")
    print(f"   Details: \n{most_expensive_car}")

    toyota_cars = df_auto_cleaned[df_auto_cleaned['company'] == 'toyota']
    print("\n3) Toyota car details:")
    print(toyota_cars)

    cars_per_company = df_auto_cleaned['company'].value_counts()
    print("\n4) Total cars per company:")
    print(cars_per_company)

    highest_prices_per_company = df_auto_cleaned.loc[df_auto_cleaned.groupby('company')['price'].idxmax()]
    print("\n5) Highest priced car of each company:")
    print(highest_prices_per_company[['company', 'price', 'body-style']])

    avg_mileage_per_company = df_auto_cleaned.groupby('company')['average-mileage'].mean()
    print("\n6) Average mileage per company:")
    print(avg_mileage_per_company)

    cars_sorted_by_price = df_auto_cleaned.sort_values(by='price', ascending=False)
    print("\n7) All cars sorted by Price (Descending):")
    print(cars_sorted_by_price[['company', 'price']].head())

except FileNotFoundError:
    print(f"Error: The file '{csv_filename}' was not found.")