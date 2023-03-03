def reverse_array(arr, start, end):
    """
    Helper function to reverse a portion of an array in place.
    """
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, d):
    """
    Function to rotate an array to the left by d positions using the reversal algorithm.
    """
    n = len(arr)
    # First, reverse the first d elements of the array
    reverse_array(arr, 0, d-1)
    # Then, reverse the remaining n-d elements of the array
    reverse_array(arr, d, n-1)
    # Finally, reverse the entire array to get the left-rotated result
    reverse_array(arr, 0, n-1)

# Test the function with an example array and d = 3
arr = [1, 2, 3, 4, 5]
d = 3
rotate_array(arr, d)
print(arr)
