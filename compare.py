# Examples of using greater and less than operators

import sys

if len(sys.argv) < 4:
    print("Oops, not enough input")
    exit()

var1 = sys.argv[1]
var2 = sys.argv[3]
comp = sys.argv[2]

if comp == "<":
    if var1 < var2:
        print("{0} is less than {1}".format(var1, var2))
    elif var1 == var2:
        print("{0} is equal {1}".format(var1, var2))
    else:
        print("{0} is not less than {1}".format(var1, var2))

if comp == ">":
    if var1 > var2:
        print("{0} is greater than {1}".format(var1, var2))
    elif var1 == var2:
        print("{0} is equal {1}".format(var1, var2))
    else:
        print("{0} is not greater than {1}".format(var1, var2))

        