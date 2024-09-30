import itertools

# Define the file paths
files = [
    'controlxi_1.txt',
    'controlxi_2.txt',
    'controlxi_3.txt',
    'controlxi_4.txt',
    'xi.txt'
    ]

# Function to read lines from a file and return a set of lines (normalized)
def read_file_lines_normalized(file_path):
    with open(file_path, 'r') as f:
        return set(line.strip() for line in f.readlines())  # Strip to remove leading/trailing whitespace

# Read lines from all files and store them in a dictionary
file_lines = {file: read_file_lines_normalized(file) for file in files}

# Generate all possible pairs of files
file_pairs = itertools.combinations(files, 2)

# Find and print common lines for each pair of files
for file1, file2 in file_pairs:
    common_lines = file_lines[file1].intersection(file_lines[file2])
    
    print(f"Common lines between {file1} and {file2}:")
    if common_lines:
        for line in common_lines:
            print(f"  {line}")
    else:
        print("  No common lines found.")
    print("-" * 40)
