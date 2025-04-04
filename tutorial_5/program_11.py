import pandas as pd
import matplotlib.pyplot as plt
import io

sales_csv_data = """month_number,facecream,facewash,toothpaste,bathingsoap,shampoo,moisturizer,total_units,total_profit
1,2500,1500,5200,9200,1200,1500,21100,211000
2,2630,1200,5100,6100,2100,1200,18330,183300
3,2140,1340,4550,9550,3550,1340,22470,224700
4,3400,1130,5870,8870,1870,1130,22270,222700
5,3600,1740,4560,7760,1560,1740,20960,209600
"""
csv_filename = "sales_data.csv"
with open(csv_filename, 'w') as f:
    f.write(sales_csv_data)
print(f"Dummy file '{csv_filename}' created.")

try:
    df_sales = pd.read_csv(csv_filename)
    print("\nSales Data Head:")
    print(df_sales.head())

    plt.figure(figsize=(10, 5))
    plt.scatter(df_sales['month_number'], df_sales['toothpaste'], c='blue', marker='o')
    plt.title('Toothpaste Sales per Month')
    plt.xlabel('Month Number')
    plt.ylabel('Toothpaste Units Sold')
    plt.xticks(df_sales['month_number'])
    plt.grid(True)
    print("\n1) Displaying Scatter Plot for Toothpaste Sales...")
    plt.show()

    plt.figure(figsize=(12, 6))
    bar_width = 0.35
    months = df_sales['month_number']
    plt.bar(months - bar_width/2, df_sales['facecream'], bar_width, label='Face Cream', color='skyblue')
    plt.bar(months + bar_width/2, df_sales['facewash'], bar_width, label='Face Wash', color='lightcoral')
    plt.title('Face Cream and Face Wash Sales per Month')
    plt.xlabel('Month Number')
    plt.ylabel('Units Sold')
    plt.xticks(months)
    plt.legend()
    plt.grid(axis='y', linestyle='--')
    print("\n2) Displaying Bar Chart for Face Cream & Face Wash Sales...")
    plt.show()

    product_columns = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
    total_sales_per_product = df_sales[product_columns].sum()

    plt.figure(figsize=(8, 8))
    plt.pie(total_sales_per_product, labels=total_sales_per_product.index, autopct='%1.1f%%', startangle=140)
    plt.title('Total Sales Distribution per Product for the Year')
    print("\n3) Displaying Pie Chart for Total Product Sales...")
    plt.show()
    print("\n   Total Sales per Product:")
    print(total_sales_per_product)

except FileNotFoundError:
    print(f"Error: The file '{csv_filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")