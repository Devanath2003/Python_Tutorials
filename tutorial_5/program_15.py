import os

cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")

try:
    items_in_cwd = os.listdir(cwd)

    print("\nItems in the current working directory:")
    if items_in_cwd:
        for item in items_in_cwd:
            print(f"- {item}")
    else:
        print("(Directory is empty)")

except FileNotFoundError:
    print(f"Error: The directory '{cwd}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to access contents of '{cwd}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")