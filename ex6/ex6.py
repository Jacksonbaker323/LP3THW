#setting the variable types of people to 10
types_of_people = 10

#Creating an f-string that will print out a string with a variable in it
x = f"There are {types_of_people} types of people"

#Setting some variables to be used in the f-string below
binary = "binary"
do_not = "don't"

#another f-string with variables in it defined above.
y = f"Those who know {binary} and those who {do_not}."

#Printing the two f-strings that we created above to write out the joke to the screen
print(x)
print(y)

# Printing the joke from the variables with additionally formatted strings
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Setting the variable hilarious to the literal value False
hilarious = False

#Creating a string with a placeholder for a variable that can be added later
joke_evaluation = "Isn't that joke so funny?! {}"

#Printing out the joke_evaluation string with the {} replaced by the value in the `hilarious` variable
print(joke_evaluation.format(hilarious))

#Creating two strings
w = "This is the left side of..."
e = "a string with a right side."

# Concatenating the above strings together.
print(w + e)
