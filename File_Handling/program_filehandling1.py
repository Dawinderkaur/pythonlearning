#--------------------------------------File Handling --------------------------------
#File handling is an essential part of python dealing with file I/O

#Types of file modes:
#When you open a file in Python, you use one of the following file modes:
# 'r' : Read (default mode). Opens the file for reading only.
# 'w' : Write. Opens the file for writing (overwrites the file if it exists).
# 'a' : Append. Opens the file for writing but does not overwrite, it appends data.
# 'x' : Exclusive creation. Opens the file for writing, but only if it does not already exist.
# 'b' : Binary. Used to handle non-text files (e.g., images, videos, etc.).
# 't' : Text (default). Used for text files.

#-----------------------------1. Opening a File-----------------------------------------------------
# Use the open() function. It returns a file object, which you can use to read or write to the file.
# Syntax
#file_object = open('filename', 'mode')

# Example
file = open('example1.txt', 'r')  # Open a file for reading

###########################################################################################################

#-------------------------------------------2. Closing a File-----------------------------------------------------
# Close a file after performing the operations.
# This ensures that all resources are freed and changes are saved.

file.close()

###########################################################################################################

#-------------------------------------------3. Reading from a File-----------------------------------------
# read(): Reads the entire content of the file.
# Reading the entire file content
file = open('example1.txt', 'r')
content = file.read()
print(content)
file.close()

#readline(): Reads a single line from the file.
# Reading line by line
file = open('example1.txt', 'r')
line = file.readline()
while line:
    print(line, end='')  # end='' prevents adding an extra newline
    line = file.readline()
file.close()

# readlines(): Reads all lines and returns a list of lines.
#### Example using readlines():
file = open('example1.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line, end='')
file.close()

###########################################################################################################

#-----------------------------------------5. Writing to a File----------------------------------------------
#- **`write()`**: Writes a string to the file. It does not add a newline automatically.
#- **`writelines()`**: Writes a list of strings to the file.

#### Example of writing to a file:
# Writing text to a file
file = open('example2.txt', 'w')
file.write("Hello, this is a test file.\n")
file.write("Let's add another line.")
file.close()

#### Example using `writelines()`:
lines = ["First line\n", "Second line\n", "Third line\n"]
file = open('example3.txt', 'w')
file.writelines(lines)
file.close()

###########################################################################################################

#-----------------------------6. Appending to a File---------------------------------------------------
#Add new content to an existing file without overwriting the old data, use the `'a'` mode (append).

file = open('example4.txt', 'a')
file.write("This is an additional line.\n")
file.close()

###########################################################################################################

#-----------------------------7. Using `with` Statement (Context Manager)---------------------------------
#The `with` statement automatically takes care of closing the file, even if an error occurs while the file is open.
# It’s considered good practice to use it.

# Example with `with` statement:
# Reading from a file using 'with'
with open('example5.txt', 'r') as file:
    content = file.read()
    print(content)

# Writing to a file using 'with'
with open('example5.txt', 'w') as file:
    file.write("This is a file written using 'with' context manager.")

###########################################################################################################

#-----------------------------8. File Handling with CSV Files-----------------------------------------------
#CSV files are a common format for storing tabular data. You can use Python's `csv` module to read and write CSV files.

import csv
# Writing to a CSV file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])  # Writing headers
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'San Francisco'])

# Reading from a CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


###########################################################################################################

#-----------------------------9. File Handling with JSON------------------------------------------------
#For working with JSON (JavaScript Object Notation) data, Python provides the `json` module.

import json

# Writing to a JSON file
data = {"name": "Alice", "age": 30, "city": "New York"}
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

# Reading from a JSON file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)
    print(data)

###########################################################################################################

#------------------------------------10. Checking File Existence-----------------------------------------
#Before opening a file, you might want to check if it exists. You can use the `os` module.

import os

if os.path.exists('example.txt'):
    print("File exists!")
else:
    print("File does not exist.")

###########################################################################################################

#---------------------------------------11. Working with Binary Files---------------------------------------
#To read or write binary data (like images), you can use the `'rb'` (read binary) and `'wb'` (write binary) modes.

# Example of reading a binary file:
with open('image.png', 'rb') as file:
    data = file.read()
    print(data)  # binary data

###########################################################################################################

#----------------------------------------------Key Takeaways--------------------------------------------------
# - **Modes**: Be mindful of file modes (`r`, `w`, `a`, etc.).
# - **Context Manager (`with`)**: Always use the `with` statement for automatic file handling.
# - **File Operations**: Learn how to read, write, append, and handle files efficiently.
# - **CSV and JSON**: Know how to work with CSV and JSON file formats.
# - **Binary Files**: Understand how to handle binary data (e.g., images).



