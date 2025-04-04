import pandas as pd
import io

data_string = """Reg_no,Name,Sub_Mark1,Sub_Mark2,Sub_Mark3
10001,Jack,76,88,76
10002,John,77,84,79
10003,Alex,74,79,81
"""

data_io = io.StringIO(data_string)

df_marks = pd.read_csv(data_io)

csv_filename = 'student_marks.csv'

df_marks.to_csv(csv_filename, index=False)

print(f"Data successfully written to {csv_filename}")
print("\nDataFrame content:")
print(df_marks)