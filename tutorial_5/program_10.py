import pandas as pd
import matplotlib.pyplot as plt

student_data = {
    'rollno': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'name': ['Anil', 'Bina', 'Chetan', 'Dipa', 'Esha', 'Firoz', 'Gita', 'Hari', 'Ishaan', 'Jaya'],
    'place': ['Mumbai', 'Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Delhi', 'Mumbai', 'Kolkata', 'Delhi', 'Chennai'],
    'mark': [85, 92, 78, 85, 90, 65, 78, 88, 92, 78]
}
df_stud = pd.DataFrame(student_data)
csv_filename = 'stud.csv'
df_stud.to_csv(csv_filename, index=False)
print(f"Dummy file '{csv_filename}' created.")

try:
    print("\na) Reading and displaying file contents:")
    df_stud = pd.read_csv(csv_filename)
    print(df_stud)

    print("\nb) Setting 'rollno' as index:")
    df_stud_indexed = df_stud.set_index('rollno')
    print(df_stud_indexed)

    print("\nc) Displaying 'name' and 'mark' columns:")
    print(df_stud[['name', 'mark']])

    print("\nd) Displaying 'rollno', 'name', 'mark' sorted by 'name':")
    print(df_stud.sort_values(by='name')[['rollno', 'name', 'mark']])

    print("\ne) Displaying 'rollno', 'name', 'mark' sorted by 'mark' (descending):")
    print(df_stud.sort_values(by='mark', ascending=False)[['rollno', 'name', 'mark']])

    avg_mark = df_stud['mark'].mean()
    median_mark = df_stud['mark'].median()
    mode_mark = df_stud['mark'].mode()
    print("\nf) Statistics for 'mark':")
    print(f"   Average: {avg_mark}")
    print(f"   Median: {median_mark}")
    print(f"   Mode(s): {list(mode_mark)}")

    min_mark = df_stud['mark'].min()
    max_mark = df_stud['mark'].max()
    print("\ng) Minimum and Maximum marks:")
    print(f"   Minimum: {min_mark}")
    print(f"   Maximum: {max_mark}")

    var_mark = df_stud['mark'].var()
    std_dev_mark = df_stud['mark'].std()
    print("\nh) Variance and Standard Deviation of marks:")
    print(f"   Variance: {var_mark:.2f}")
    print(f"   Standard Deviation: {std_dev_mark:.2f}")

    print("\ni) Displaying histogram of marks (plot window will open):")
    plt.figure(figsize=(8, 5))
    plt.hist(df_stud['mark'], bins=5, edgecolor='black')
    plt.title('Histogram of Student Marks')
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

    print("\nj) DataFrame after removing the 'place' column:")
    df_no_place = df_stud.drop(columns=['place'])
    print(df_no_place)

except FileNotFoundError:
    print(f"Error: The file '{csv_filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")