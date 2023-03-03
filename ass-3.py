#Assignment-03

def binary_search(arr, x):
    # Set initial low and high indices
    low = 0
    high = len(arr) - 1

    # Keep dividing the search space in half until we find the element or exhaust the search space
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    # If we haven't returned yet, the element is not in the list
    return False
my_list = [1, 3, 4, 6, 8, 9, 11, 13, 14]

# Check if 6 is in the list
if binary_search(my_list, 15):
    print("15 is in the list")
else:
    print("15 is not in the list")


#Output-
#15 is not in the list