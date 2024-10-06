def remove_duplicate_lines(file_path, output_file=None):
    # Set to store unique lines
    seen_lines = set()
    
    # List to store the unique lines (one copy of each duplicate)
    unique_lines = []

    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Strip leading/trailing whitespace (optional)
            stripped_line = line.strip()

            # Check if the line is already seen
            if stripped_line not in seen_lines:
                # If it's not a duplicate, add it to the list and mark as seen
                unique_lines.append(line)  # Keep original line formatting
                seen_lines.add(stripped_line)

    # Write the unique lines back to the file (or to a new file)
    output_path = output_file if output_file else file_path
    with open(output_path, 'w') as file:
        file.writelines(unique_lines)

    print(f"Processed {file_path}. Duplicates removed. Output saved to {output_path}.")

# Example usage: Replace 'yourfile.txt' with the path to your text file
# Optionally, provide an output file to avoid overwriting the original file
remove_duplicate_lines('cleaned_file.txt', 'cleaned_file_1.txt')  # or just 'yourfile.txt' to overwrite
