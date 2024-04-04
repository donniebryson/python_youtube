# Range returns elements for iteration the same as a tuple, set, or list.
# The function can take up to three arguments:
# range(START_NUMBER, END_NUMBER, STEP_NUMBER)
# The only one required is the END_NUMBER.

#Notice below that the range starts with 0 and ends with 9. END_NUMBER is 10 because it 
# there is only one argument. 
print("range(10)")
for x in range(10):
    print(x)

# If you want to start with 1 then set the START_NUMBER and it goes before the STOP_NUMBER.
print("range(1,10)")
for x in range(1, 10):
    print(x)

# If you need to step by a particular integer, you can add the STEP_NUMBER
print("range(1,10,3)")
for x in range(0, 10, 3):
    print(x)

for print_it in range(5):
    print("Printing FIVE times")

test_it = 10
if test_it in range(5):
    print("test_it is between 0 and 4")
elif test_it in range(5, 10):
    print("test_it is between 5 and 10")
else:
    print("test_it is out of range.")

# You could use a list to make the same test
if test_it in (0, 1, 2, 3, 4):
    print("test_it is between 0 and 4 ")
elif test_it in (5, 6, 7, 8, 9):
    print("test_it is between 5 and 10")
else:
    print("test_it is out of range")

# Important note! range takes less memory and it is more pronounced the range
print(range(10))
print((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))

