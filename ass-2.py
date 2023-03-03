#Assignment-02
#ask the user for a number. depending on weather the number is even or odd , print out an appropriate message to the user. 

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")


# Output:
#Enter a number: 7
#7 is odd.