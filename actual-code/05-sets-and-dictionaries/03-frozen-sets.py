complex_set = frozenset([True, 0, 0.1, "Hello", (1,2,3)])

# save memory, they become immutable, can be used as elements in other sets

print(complex_set)

complex_set = set(complex_set)

complex_set.add("1")

