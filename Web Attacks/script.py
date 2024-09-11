import csv
import os

# Get the current directory (where the script is located)
current_directory = os.path.dirname(os.path.abspath(__file__))

# CSV file name (assumed to be in the same directory)
csv_file_name = 'webvuln.csv'

# Construct the full path to the CSV file
csv_file_path = os.path.join(current_directory, csv_file_name)

# Read the CSV file and create .md files
with open(csv_file_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        if row:  # Check if the row is not empty
            name = row[0].strip()  # Get the name from the first (and only) column
            filename = f"{name}.md"
            file_path = os.path.join(current_directory, filename)
            
            # Create and write to the .md file
            with open(file_path, 'w') as mdfile:
                mdfile.write(f"# {name}\n\nThis is a markdown file for {name}.")

print("Markdown files have been created successfully in the current directory.")