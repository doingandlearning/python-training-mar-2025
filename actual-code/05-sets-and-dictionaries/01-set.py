# list, dictionary
# tuple
# set

empty_set = set()

print(empty_set)
print(type(empty_set))

fruit_list = {"apple", "banana", "cherry", "dragonfruit"}
print(fruit_list)  # order is non-deterministic
print("apple" in fruit_list)

fruit_list.add("apple")  # doesn't allow duplicates!
print(fruit_list)

list_of_accelerators = ["LHC", "LPC", "LHC"]
unique_accelerators = list(set(list_of_accelerators))
print(unique_accelerators)

fruit_list.add("kiwi")  # equivalent [].append()
print(fruit_list)

fruit_list.update(["pear", "apple", "orange"])  # equivalent [].extend()
print(fruit_list)