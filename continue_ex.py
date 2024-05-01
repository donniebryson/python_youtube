# Using continue and break
print("Using continue. Skip the rest of this loop and go to the next one.")
for num in range(5):
    if num == 3:
        print("I was three", num)
        continue
    print("I was not three", num)

print("Using break. Exit the loop.")
for num in range(5):
    if num == 3:
        print("I was three", num)
        break
    print("I was not three", num)


