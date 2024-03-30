import os
# The os module gives python access to the operating system functionality like directories and files. 

# display the current working directory of the script
print(os.getcwd())

# display the current termincal size of the script. 
print(os.get_terminal_size())

# Special note for Windows users: either preface your directory/file string with r (ex: r"C:\temp") or double slash
# like this: "C:\\tmp\\test.txt")
#os.chdir("C:\tmp")
os.chdir("C:\\tmp")
os.chdir(r"C:\tmp")
print(os.getcwd())

# Note: The working directory is only changed during the running of the script. 
# The system returns to its original location after the script runs. 

# making a directory
os.mkdir(r"C:\tmp\test_dir")
os.listdir(r"C:\tmp")
print("Removing test_dir directory")
os.rmdir(r"C:\tmp\test_dir")
print(os.listdir(r"C:\tmp"))

# os.path.join combines fields into a valid path name regardless of operating system. 
# open() and read() are used to bring file input into the program. 

try:
    filename = os.path.join("C:\\tmp\\", "test.txt")
    f = open(filename, 'r')
    text = f.read()
    f.close()
    print(text)
except IOError:
    print('Oops, cannot read file: ' + filename)