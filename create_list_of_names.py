import csv

# Function to read a specific column from a CSV file and return it as a list
def csv_column_to_list(csv_file_path, column_name):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        column_data = [row[column_name] for row in reader]
    return column_data

# Path to the CSV file
csv_file_path = '/Users/miki/Downloads/list_of_usernames.csv'

# Column name to extract
column_name = 'Name'

# Get the list from the CSV column
names_list = csv_column_to_list(csv_file_path, column_name)

# Print the list to verify
print(names_list)
