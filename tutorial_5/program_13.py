import pandas as pd
import io

employee_csv_data = """name,gender,start_date,salary,team
Alice,Female,2020-03-15,75000,Engineering
Bob,Male,2019-11-01,80000,Sales
Charlie,Male,2021-07-20,70000,Engineering
Diana,Female,2018-05-10,95000,Marketing
Ethan,Male,2022-01-05,60000,Sales
Fiona,Female,2019-08-25,110000,Engineering
George,Male,2023-02-18,65000,Support
Hannah,Female,2020-09-30,78000,Marketing
Ian,Male,2021-12-12,82000,Support
"""
csv_filename = "employee.csv"
with open(csv_filename, 'w') as f:
    f.write(employee_csv_data)
print(f"Dummy file '{csv_filename}' created.")

try:
    df_emp = pd.read_csv(csv_filename)
    print("\nOriginal Employee Data:")
    print(df_emp)

    print("\n1) First 7 records:")
    print(df_emp.head(7))

    print("\n2) Employee names in alphabetical order:")
    print(df_emp['name'].sort_values().tolist())

    highest_salary_employee = df_emp.loc[df_emp['salary'].idxmax()]
    print(f"\n3) Employee with highest salary: {highest_salary_employee['name']} (Salary: {highest_salary_employee['salary']})")

    male_employees = df_emp[df_emp['gender'] == 'Male']['name']
    print("\n4) Names of male employees:")
    print(male_employees.tolist())

    unique_teams = df_emp['team'].unique()
    print("\n5) Unique teams employees belong to:")
    print(unique_teams.tolist())

except FileNotFoundError:
    print(f"Error: The file '{csv_filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")