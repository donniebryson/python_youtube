# Iterables and all()/any()
# Both all() and any() deal with the truth table across the entire scope of an iteratable. 


# By iterable, we mean a list, tuple, dict, or set. 
my_list = ["one", 2, "three"] # mutable 
my_tuple = ("one", 2, "three") # immutable 
my_set = {"one", 2, "three"} # unordered, unchangeable, and does not allow duplicate values
my_dict = {"one": "one", "two": 2, "three": "three"} # mutable with an index


# We have to be careful what we mean by true. It is obvious when talking about bools. However,
# numbers and strings are a little confusing. 
print("This is True because it has characters: ", bool("This has some characters"))
print("This is False because it has no characters: ", bool(""))
print("This is True because it is not 0: ", bool(1))
print("This is False because it is 0: ", bool(0))

# Any() holds true if any of the elements are true
my_test_list = [1,0,0]
print("Using any() with this list: ", my_test_list, any(my_test_list))
print("Using all() with this list: ", my_test_list, all(my_test_list))
my_test_list[0] = 0 # set the 0 
print("Using any() with this list: ", my_test_list, any(my_test_list))
my_test_list = [1 for x in my_test_list] # set all values to 1
print("Using all() with this list: ", my_test_list, all(my_test_list))