# Let's read the contents of the 'xi.txt' file and convert it into a CSV file
file_path = 'xi.txt'
output_csv = 'xi.csv'

# Reading the content of the text file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Cleaning up lines and converting to CSV format
lines = [line.strip() for line in lines if line.strip()]  # Remove any empty lines and extra spaces

# Writing to CSV file
import csv

with open(output_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["xi"])  # Adding a header
    for line in lines:
        writer.writerow([line])