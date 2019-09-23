
# Create a function that prints out info given counts
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man, that's enough for a party!")
    print("Get a blanket. \n")

# Pass some numbers directly to the function
print("We can just give the function numbers directly.")
cheese_and_crackers(20, 30)

# Set some variables and pass them to the function
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Pass some numbers directly, but as the result of math operations
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Pass our variables, but with math operations applied to them 
print("We can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)