msg = "Sort One list using the other list"
print(msg)

# create two lists
list1 = [4, 2, 1, 3]
list2 = ['d', 'b', 'a', 'c']

# sort list2 based on the order of elements in list1
list2_sorted = [x for _, x in sorted(zip(list1, list2))]

# print the sorted list
print(list2_sorted)
