def find_duplicate_lines(file_path):
    # Set to store unique lines
    seen_lines = set()
    # List to store duplicate lines
    duplicate_lines = []
    count =0

    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Strip leading/trailing whitespace (optional)
            stripped_line = line.strip()

            # Check if the line is already seen
            if stripped_line in seen_lines:
                # If it is a duplicate, add it to the list
                duplicate_lines.append(stripped_line)
            else:
                # Otherwise, add the line to the set of seen lines
                seen_lines.add(stripped_line)

    # Check if there are any duplicates
    if duplicate_lines:
        print("Duplicate lines found:")
        for line in duplicate_lines:
            print(line)
            count+=1

    else:
        print("No duplicate lines found.")
    
    print(count)

# Replace 'yourfile.txt' with the path to your text file
find_duplicate_lines('cleaned_file_1.txt')
