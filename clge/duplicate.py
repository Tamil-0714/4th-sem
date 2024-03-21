# Aim : 
    # to write Piton program for remove duplicated from a list using For loop

input_list = [1, 2, 3, 4, 2, 3, 5]
unique_list = []
for item in input_list:
    if item not in unique_list:
        unique_list.append(item)
print("Original list:", input_list)
print("List with duplicates removed:", unique_list)


"""
Output : 
    Original list: [1, 2, 3, 4, 2, 3, 5]
    List with duplicates removed: [1, 2, 3, 4, 5]

"""