test_it = 10
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