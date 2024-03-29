import os

# display the current working directory of the script
print(os.getcwd())

# display the current termincal sizeo of the script
print(os.get_terminal_size())


try:
    fp = open("myfile")
except PermissionError:
    return "some default data"
else:
    with fp:
        return fp.read()
    