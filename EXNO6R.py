import os
# Creating a directory
def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
# Deleting a directory
def delete_directory(directory_name):
    try:
        os.rmdir(directory_name)
        print(f"Directory '{directory_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"Directory '{directory_name}' does not exist.")
    except OSError as e:
        print(f"Error: {e}. Unable to delete directory '{directory_name}'.")
# Writing to a file
def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
            print(f"Content written to '{file_name}' successfully.")
    except IOError:
        print(f"Error writing to file '{file_name}'.")
# Reading from a file
def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        print(f"Content from '{file_name}':")
        print(content)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except IOError:
        print(f"Error reading file '{file_name}'.")
# Directory name
directory_name = "TestDirectory"
# File name and content
file_name = "test_file.txt"
file_content = "This is a test file. Hello, world!"
# Create a directory
create_directory(directory_name)
# Write to a file
write_to_file(file_name, file_content)
# Read from a file
read_from_file(file_name)
# Delete a directory
delete_directory(directory_name)
