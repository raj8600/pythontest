#Assignment-08
#Finds the sum of the series up to n terms, where n is 5:
# Set the value of n
n = 5

# Initialize the sum variable
sum = 0

# Calculate the sum of the series up to n terms
for i in range(1, n+1):
    term = i**2
    sum += term

# Print the sum of the series
print("The sum of the series up to", n, "terms is", sum)

#Output-
#The sum of the series up to 5 terms is 55