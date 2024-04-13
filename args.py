# Import the standard argparse library. This comes with the standard python installation. 
import argparse

# Create the parsing instance
parser = argparse.ArgumentParser(prog='DevMoney',
                    description='Calculate the cost of a developer per week',
                    epilog='Total based on rates given')

# Positional arguments. These are required unless the program is ran with '-h' to generate the help file. 
parser.add_argument("developer", help="Enter the name of the developer")
parser.add_argument("hourly_rate", help="Enter hourly rate for developer", type=float)
parser.add_argument("hours_per_week", help="Enter hours worked per week", type=int, choices=range(0,41, 8))

# An option argument. 
parser.add_argument("--is_contractor", "-c", action="store_true")
parser.add_argument("--cur_year", "-y", )

args = parser.parse_args()

print(args.developer, "-- Weekly rate: ", args.hourly_rate * args.hours_per_week)
if args.is_contractor:
    print("Contractor")
else:
    print("Not Contractor")

if args.cur_year:
    print("Year: ", args.cur_year)

    
