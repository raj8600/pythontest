#Assignment-04
#Palindorme program
# Ask the user for a string
string = input("Enter a string: ")

# Reverse the string
reverse_string = string[::-1]

# Check if the string is equal to its reverse
if string == reverse_string:
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")


#Output-
#Enter a string: nitin
#The string is a palindrome!

