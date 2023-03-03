#Assignment -07
#Cub of numbers
# Ask the user for the number
n = int(input("Enter a number: "))

# Print the cubes of numbers from 1 to n
for i in range(1, n+1):
    cube = i ** 3
    print("The cube of", i, "is", cube)


#Output-
#Enter a number: 5
#The cube of 1 is 1
#The cube of 2 is 8
#The cube of 3 is 27
#The cube of 4 is 64
#The cube of 5 is 125