# A match statement is similar to switch in other languages. 
# Match compares a value to patterns with a case statement. 
""" """ my_size = ("small", "medium", "large")

for this_size in my_size:
    match this_size:
        case "small":
            print(this_size, ": I am small.")
        case "medium":
            print(this_size, ": I am medium.")
        case "large":
            print(this_size, ": I am large.")
 """
 """x = 5
y = 9
points = ((0,0), (0,y), (x,0), (x, y), ("Make Error"))
for p in points:
    match p:
        case (0, 0):
            print(f"{p} Origin")
        case (0, y):
            print(f"{p} Y={y}")
        case (x, 0):
            print(f"{p} X={x}")
        case (x, y):
            print(f"{p} X={x}, Y={y}")
