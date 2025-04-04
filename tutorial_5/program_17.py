import pandas as pd
import io

student_cgpa_data = """Name,Branch,Year,CGPA
Aditya,CSE,3,9.2
Bhaskar,ECE,2,8.5
Charu,CSE,4,9.5
David,MECH,3,7.8
Elina,CSE,2,9.1
Farhan,ECE,4,8.9
Gauri,MECH,2,8.2
Harish,CSE,3,8.8
Ishita,CSE,4,9.8
Jatin,ECE,3,9.0
"""
csv_filename = "student_cgpa.csv"
with open(csv_filename, 'w') as f:
    f.write(student_cgpa_data)
print(f"Dummy file '{csv_filename}' created with CGPA data.")

try:
    df_stud_cgpa = pd.read_csv(csv_filename)
    print("\nStudent CGPA Data:")
    print(df_stud_cgpa)

    average_cgpa = df_stud_cgpa['CGPA'].mean()
    print(f"\nAverage CGPA of all students: {average_cgpa:.2f}")

    high_cgpa_students = df_stud_cgpa[df_stud_cgpa['CGPA'] > 9]
    print("\nDetails of students with CGPA > 9:")
    print(high_cgpa_students)

    high_cgpa_cse_students = df_stud_cgpa[(df_stud_cgpa['Branch'] == 'CSE') & (df_stud_cgpa['CGPA'] > 9)]
    print("\nDetails of CSE students with CGPA > 9:")
    print(high_cgpa_cse_students)

    student_max_cgpa = df_stud_cgpa.loc[df_stud_cgpa['CGPA'].idxmax()]
    print("\nDetails of student with maximum CGPA:")
    print(student_max_cgpa)

    avg_cgpa_by_branch = df_stud_cgpa.groupby('Branch')['CGPA'].mean()
    print("\nAverage CGPA of each branch:")
    print(avg_cgpa_by_branch)

except FileNotFoundError:
    print(f"Error: The file '{csv_filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")