import os
import pandas as pd

def get_valid_path(prompt):
    while True:
        path = input(prompt)
        if os.path.isfile(path) and path.endswith(('.xlsx', '.csv')):
            return path
        print("Invalid path. Please enter a valid path to a spreadsheet.")

def compare_spreadsheets(path1, path2):
    df1 = pd.read_excel(path1) if path1.endswith('.xlsx') else pd.read_csv(path1)
    df2 = pd.read_excel(path2) if path2.endswith('.xlsx') else pd.read_csv(path2)
    if df1.equals(df2):
        print("The spreadsheets are identical.")
        return
    output_dir = os.path.join(os.path.dirname(path1), "comparison-output")
    os.makedirs(output_dir, exist_ok=True)
    log_path = os.path.join(output_dir, "comparison_log.txt")
    with open(log_path, 'w') as log_file:
        log_file.write("The following differences were found:\n")
        for row in range(df1.shape[0]):
            for col in range(df1.shape[1]):
                if df1.iloc[row, col] != df2.iloc[row, col]:
                    log_file.write(f"Difference in row {row + 1}, column {df1.columns[col]}: "
                                   f"{df1.iloc[row, col]} vs {df2.iloc[row, col]}\n")
    print(f"Differences found. Log written to {log_path}.")

if __name__ == '__main__':
    path1 = get_valid_path("Enter the path to the first spreadsheet: ")
    path2 = get_valid_path("Enter the path to the second spreadsheet: ")
    compare_spreadsheets(path1, path2)
