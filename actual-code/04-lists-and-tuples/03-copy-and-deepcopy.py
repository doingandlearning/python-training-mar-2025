import copy

number_list = [1, 2, 3, 4]
number_list_2 = number_list


number_list_2.append(5)
print(number_list_2)
print(number_list)

list_of_lists = [[1,2], [3,4]]
list_of_lists_copy = copy.deepcopy(list_of_lists)

list_of_lists_copy[1].append(5)
list_of_lists.append(6)
print(list_of_lists)
print(list_of_lists_copy)