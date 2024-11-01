import string

def remove_punctuation(text):
    punctuation_table = str.maketrans('', '', string.punctuation)
    text_without_punctuation = text.translate(punctuation_table)
    return text_without_punctuation

def text_to_lowercase(text):
    # Convert text to lowercase
    text_lower = text.lower()
    return text_lower

# Read text from file
input_file_path = 'questions.txt'  # Update with your input file path
output_file_path = 'output_file.txt'  # Update with your output file path

with open(input_file_path, 'r') as input_file:
    text = input_file.read()

# Remove punctuation
text_without_punctuation = remove_punctuation(text)

# Convert text to lowercase
text_lower = text_to_lowercase(text_without_punctuation)

# Write processed text to another file
with open(output_file_path, 'w') as output_file:
    output_file.write(text_lower)

print("Processed text has been saved to:", output_file_path)
