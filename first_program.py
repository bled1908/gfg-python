print("Subhadeep Roy")

# print() Function Syntax 
# Syntax : print(value(s), sep= ' ', end = '\n', file=file, flush=flush)

# Parameters: 

# value(s): Any value, and as many as you like. Will be converted to a string before printed
# sep='separator' : (Optional) Specify how to separate the objects, if there is more than one.Default :' '
# end='end': (Optional) Specify what to print at the end.Default : '\n'
# file : (Optional) An object with a write method. Default :sys.stdout
# flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False
# Return Type: It returns output to the screen.
# it is not necessary to pass arguments in print() function
# \n: This string literal is used to add a new blank line while printing a statement.
# "": An empty quote ("") is used to print an empty line.
# Concatenated Strings with +
# Note: As sep, end, flush, and file are keyword arguments their position does not change the result of the code. 

# print() Function with file parameter
# This code is writing the data in the print() function to the text file. 
# print('Welcome to GeeksforGeeks Python world.!!', file=open('Testfile.txt', 'w'))

# Line Continuation - \ is a explicit line continuation character in Python.
sentence = "This is a very long sentence that we want to" \ 
    " split over multiple lines for better readability."
print(sentence)

# For mathematical operations
total = 1 + 2 + 3 + \ 
    4 + 5 + 6 + \
    7 + 8 + 9
print(total)

# Note: Using a backslash does have some pitfalls, such as if there's a space after the backslash, it will result in a syntax error.

# Implicit Continuation
# Python implicitly supports line continuation within parentheses (), square brackets [], and curly braces {}. This is often used in defining multi-line lists, tuples, dictionaries, or function arguments.

# Line continuation within square brackets '[]'
numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

print(numbers)

# Python input() Function Syntax
# Syntax: input(prompt)

# Parameter:

# Prompt: (optional) The string that is written to standard output(usually screen) without newline.
# Return: String object