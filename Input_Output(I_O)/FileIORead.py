# Opening a file
file  = open("C:\\Users\\nEW u\\Downloads\\sample.txt", "r")     # Here 'r' is for read command
# return type = FileNotFoundError

# Opening a file provides a so-called “file handle.” A file handle can be seen as an access point to the file.
# It contains a “pointer” that indicates a particular place in the file. That pointer is used when you read
# from or write to the file.For instance, when you read from the file, it starts reading at the
# pointer, and moves the pointer forward in the file.
#
# When you open a file, the pointer is placed at a particular spot in the file, depending on
# how you opened the file. If you opened the file for reading only, the pointer is placed at the
# start of the file. The same is true when you open the file for both reading and writing. If
#     you open the file for “appending” (i.e., to place new data at the file’s end), the file pointer
# is positioned at the end of the file. Lastly, if you open a file for writing only, actually the
# file is completely emptied and the file pointer is placed at the start of the, now empty, file.
# To create a new file (i.e., a file with a name that does not exist yet), you open it for “writing
# only.”
# After opening the file, the file handle is the only access point for the file. All actions you
# perform on the file, you perform as methods for the file handle.
# Note that any operating system only allows a limited number of files to be open simultaneously.
# Therefore you should close files that you no longer need to work with.

# Moving the file pointer :
#
# The file pointer, that indicates where in a file you are working, is moved automatically.
# For instance, when you read 10 characters from a file, the file pointer indicates which is
# the first of those 10 characters, and, while reading, moves up 10 characters, so that its new
# position is 10 characters further in the file than before. When you deal with text files, the
# automatic movements of the file pointer are exactly what you want. You can position the
# file pointer manually using specific methods, but such methods are, in general, only used
# when dealing with binary files. Therefore, in this chapter I will ignore these methods, but
# they will be discussed in the chapter on binary files.
#
#
# Buffering
#
# When you make changes to files, these often are not stored in the files immediately. Instead,
# the operating system “buffers” the changes in memory, and “flushes” the buffers to the
# actual files when it sees a need for that. You can force the flushing of the buffers by closing
# a file. Buffers are also flushed when your program ends normally.
#
# However, when your program crashes (for instance because of a runtime error), buffers
# might not be flushed, and your files will not be updated to the point where the crash took

print(file.readline())
# The readline() method reads characters starting at the file pointer up to and including the next newline
# character, and returns them as a string.
for line in file:
    print(line)
print(file)
# O/P--> <_io.TextIOWrapper name='C:\\ROHAN\\core_java\\PythonLearning\\HelloWorld\\sample' mode='r' encoding='cp1252'>

# Now file named file-handle is empty
print(file.readline())          # no output wiuld be there

file.close()

# It is necessary to close the file which flushes the data from the buffer of the operating system,
# however file flushed when program closes without any error or interruption
# if some hoe the file is not closed after writing then file cannot be moved or edited externally

# 'with' keyword --> using 'with' keyword with object can destroy them automatically when no longer the are needed
# if there is any error in 'with' statement neutralizes the error preventing the program from being stopped
print('#'*80)

with open('C:\\Users\\nEW u\\Downloads\\sample.txt', "r") as file:
    for line in file:
        if 'jab' in line.lower():
            print(line)
print('#'*80)
with open('C:\\Users\\nEW u\\Downloads\\sample.txt', "r") as file:
    line  = file.readline()
    while line:
        print(line, end='')
        line = file.readline()

# Following code will return a whole list containing lines of the content
print('#'*80)
with open('C:\\Users\\nEW u\\Downloads\\sample.txt', "r") as file:
    lines = file.readlines()
# readlines() : reads all the lines in the file, and returns them as a list of strings.
# The strings include the newline characters.

    print(lines)

# iterating through the list
print('#'*80)
for line in lines:
    print(line, end='')

# Reversing the poem upside down
print('#'*80)
for line in lines[::-1]:
    print(line, end='')

# Now can extract data in single characters by read() method

print('$'*80)
with open('C:\\Users\\nEW u\\Downloads\\sample.txt', "r") as file:
    chars = file.read()     # It returns entire content of the file in form of String
    print(chars)
# reversing letters of each line
    for char in chars[::-1]:
        print(char, end='')

# When to use which file-reading method :
# Both the read() and readlines() method read a whole file at once. Obviously, for small files this is acceptable,
# but for long files you might not have enough memory to store the file contents efficiently. In such circumstances
# (or when you do not know the file size), you should read a file line by line with the readline() method

