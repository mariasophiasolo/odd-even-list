# creating new list from two list with condition

def create_new_list(list1, list2):
# filter odd numbers from the first list
    odd_numbers = [num for num in list1 if num % 2 != 0]

# ilter even numbers from the second list
    even_numbers = [num for num in list2 if num % 2 == 0]

# combine the two lists to create the new list
    new_list = odd_numbers + even_numbers

    return new_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
result = create_new_list(list1, list2)

print("list 1:10, 20, 25, 30, 35\nlist 2:40, 45, 60, 75, 90\n")
print("New list:", result)

