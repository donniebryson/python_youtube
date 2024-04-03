# Often we are required to use classifiers that describe data points. 
# The quick and sloppy way to do it with with simple variables as below. 
# This defines the size of things. 
size_type = "LARGE"
my_size = "LARGE"

# It will work OK with one person coding in one source file.
if (my_size == size_type):
    print("You are large")

# You can even skip the variable and hardcode the value into the source file. 
if (my_size == "LARGE"):
    print("You are large")

# But then more people start coding on the project and they are coding in multiple files.
    
if (my_size == "large"):
    print("You are large")
else:
    print("You are not large")

from enum import Enum
class SizeType(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE =  3

my_size = SizeType.LARGE
if (my_size == SizeType.LARGE):
    print("You are large")
else:
    print("You are not large")

# functional syntax
SizeType2 = Enum('SizeType2', ['SMALL', 'MEDIUM', 'LARGE'])

my_size2 = SizeType2.MEDIUM
if ( my_size2 == SizeType.MEDIUM):
    print("You are MEDIUM")
else:
    print("You are not MEDIUM")
