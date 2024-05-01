# Simple ways to combine lists

# Combine and disregard having duplicates
list1 = [0, 3, 6, 9]
list2 = [9, 12, 15]

combo1 = list1 + list2
print("Simply add the two lists together:", combo1)

# Combine without duplicates
combo2 = list1 + [x for x in list2 if x not in list1]
print("Using list comprehension to combine lists that do not contained self-contained duplicates:", combo2)

list3 = [0, 3, 6, 6, 9]
combo3 = list3 + [x for x in list2 if x not in list3]
print("List comprehension does not remove duplicates caused between lists:", combo3)
combo4 = list(set(list2 + list3))
print("Combine lists using set that removes duplicates from all sources:", combo4)

