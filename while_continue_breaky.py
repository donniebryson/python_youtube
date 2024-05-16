'''Using while, continue, and break'''

# while checks a condition at the top of the loop. 
# notice the implication here -- what you are checking can change in the loop
x = 0
while x <= 2:
    print("x value before adding", x)
    x += 1
    print("x before after adding", x)

# continue jumps to the next run of the loop
x = 0
while x <= 3:
    x +=1
    if x == 2:
        print("not printing x")
        continue
    print(x)

# break exits the loop
x = 0
while x <= 3:
    x +=1
    if x == 2:
        print("will not finish loop")
        break
    print("x is", x)

