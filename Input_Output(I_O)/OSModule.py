from os import getcwd, listdir, chdir,system
from os.path import exists, isdir, isfile, join, basename, dirname, getsize

# getcwd()   ---> Return a unicode string representing the current working directory.
print(getcwd())          # C:\ROHAN\core_java\PythonLearning\Input_Output(I_O)

# chdir() --> changes the current working directory. The new directory is provided as a string argument.
# chdir('..')         # C:\ROHAN\core_java\PythonLearning
# print(getcwd())

# listdir() returns a list of all the files and directories in the directory that is given as argument.
# The names are given in arbitrary order. Notice that they do not include the full path name.

print(listdir())

# system() gets a string argument that is a command, that Python executes on the command line.
print(help(system))

# os.path methods

# exists() : It gets a path as argument, and returns True if that path exists, and False if it does not.

print(exists('sample'))
# isfile() : It tests if the path that is supplied as argument is a file. If it is, it returns True.
# If it is not, it returns False. If the path does not exist, the function also returns False.
print(isfile('sample.txt'))
#
# isdir()
# isdir() tests if the path that is supplied as argument is a directory. If it is, it returns True.
# If it is not, it returns False. If the path does not exist, the function also returns False.
print(isdir(getcwd()))
print(isdir('sample'))
#
# join() :

# join() takes one or more parts of a path as argument, and concatenates them reasonably
# intelligently to a legal name for a path, which it returns. This means that it will add and remove slashes as needed.
# join() is particularly handy in combination with listdir()
print(join(getcwd(),'sample'))

# basename() extracts the filename from a path, and returns it.
print(basename('C:\ROHAN\core_java\PythonLearning\Input_Output(I_O)\sample'))
# it return the directory name if the path does not contains any file

# dirname() extracts the directory name from a path, and returns it.
print(dirname('C:\ROHAN\core_java\PythonLearning\Input_Output(I_O)\sample'))
#
# getsize()
# getsize() gets the size of the file that is supplied as argument, and returns it as an integer
# (representing a number of bytes). The file must exist, otherwise you get a runtime error. FileNotFoundError
print(getsize('C:\ROHAN\core_java\PythonLearning\Input_Output(I_O)\sample.txt'))