# excel-compare-diff
2 file paths are read into Pandas dataframes. It compares data in the dataframes and creates a log file output directory containing any differences found between the two files. If no differences exist it outputs a message to indicate that the files are identical. If differences are found it outputs a message and provides the path to the log file
The code defines a function named get_valid_path that prompts the user to enter a file path and checks if the path leads to an existing file with an .xlsx or .csv extension. If the path is valid, it returns the path; otherwise, it asks the user to enter a valid path to a spreadsheet.

The code also defines a function named compare_spreadsheets that takes two file paths as arguments. It reads the contents of the files into pandas DataFrames, compares the DataFrames for differences, and creates a log file that records the differences. The log file is stored in a subdirectory called "comparison-output" in the directory of the first file.

The main function uses the get_valid_path function to prompt the user for the file paths to the two spreadsheets to be compared. It then calls the compare_spreadsheets function with the two file paths as arguments.
