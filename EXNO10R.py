import re

def process_text(text):
    """
    This function processes a given text in the following ways:
    1. Counts the number of words in the text.
    2. Finds and displays all capitalized words.
    3. Replaces 'Python' with 'JavaScript' in the text.
    """

    # Count the number of words in the text
    words = text.split()
    num_words = len(words)
    print(f"Number of words in the text: {num_words}\n")

    # Find and display all capitalized words using regular expressions
    capitalized_words = re.findall(r'\b[A-Z][a-z]*\b', text)
    print("Capitalized words in the text:\n")
    for word in capitalized_words:
        print(word)

    # Replace 'Python' with 'JavaScript' in the text
    modified_text = re.sub(r'\bPython\b', 'JavaScript', text)
    print("\nModified text after replacing 'Python' with 'JavaScript':\n")
    print(modified_text)

# Example text for processing
input_text = """
Python is a widely-used programming language. It is known for its simplicity and readability.
Many developers love Python for its versatility.
"""

# Perform text processing using the function process_text(input_text)
process_text(input_text)