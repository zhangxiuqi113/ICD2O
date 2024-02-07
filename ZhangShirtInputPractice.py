# declare of a variable of type float to store the price of a shirt

fltPrice = 15.99

# output message to the user telling them the price of our shirts

print("We are selling the shirts for" , fltPrice)

# declare a variable to store the number of shirts and populate with user input

intNumShirts = int(input("How many shirts would you like to buy?"))

# calculate the cost of the shirts for the user

fltCost = intNumShirts * fltPrice

# output the cost to the user

print("Your cost for" , intNumShirts , "at" , fltPrice , "is $" , fltCost)