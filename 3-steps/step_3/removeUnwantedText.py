import os

def remove_lines_with_patterns(input_file, output_file, patterns):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if not any(pattern in line for pattern in patterns) and line.strip():
                outfile.write(line)

def process_files(input_folder, output_folder, patterns):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, file_name)
        output_file_path = os.path.join(output_folder, f"updated_{file_name}")
        remove_lines_with_patterns(input_file_path, output_file_path, patterns)
        print(f"Removed unwanted text(patterns/Pattern etc) from: {file_name}")

# Example usage
input_folder= './idf_traces/'
output_folder= './step3-updated_idf_traces'

patterns_to_remove = ['Pattern', "pattern", 'patterns', 'Patterns:', 'Longest_pattern_size']

#remove_lines_with_patterns(input_file, output_file, patterns_to_remove)
process_files(input_folder, output_folder, patterns_to_remove)

print("Unwanted text removed\n")

