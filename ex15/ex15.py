from sys import argv

# unpacks the arguments passed to argv into two different variables
script, filename = argv

# Opens the file by the name that was passed when the script was kicked off
txt = open(filename)

# Takes the txt obj that we created and uses its read function to print text
print(f"Here's your file {filename}.")
print(txt.read())

# Asks for a new filename
print("Type the filename again.")
file_again = input("> ")

# Opens that file
txt_again = open(file_again)

# Prints out the contents of that file
print(txt_again.read())

# Close the files once we're done to clean up after ourselves
txt.close()
txt_again.close()
