# file = open('example1.txt', 'r')
# content = file.read()
# print(content)
# file.close()

# Reading line by line
# file = open('example1.txt', 'r')
# line = file.readline()
# while line:
#     print(line, end='')  # end='' prevents adding an extra newline
#     line = file.readline()
# file.close()
#
# #### Example using readlines():
file = open('example1.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line, end='')
file.close()