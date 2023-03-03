def pascals_triangle(n):
    """
    Function to print Pascal's triangle up to n rows.
    """
    # Create an empty list to hold the rows of Pascal's triangle
    triangle = []

    # Loop through each row up to n
    for i in range(n):
        # Create a new list to hold the numbers in this row
        row = []
        # Loop through each number in the row
        for j in range(i+1):
            # If it's the first or last number in the row, it's a 1
            if j == 0 or j == i:
                row.append(1)
            # Otherwise, it's the sum of the two numbers above it
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # Add the row to the triangle
        triangle.append(row)

    # Print the triangle
    for row in triangle:
        print(" ".join(str(num) for num in row).center(n*2))

# Test the function with n = 5
pascals_triangle(5)
