results_fib = {1, 1, 2, 3, 5, 8, 13, 21}
results_prime = {2, 3, 5, 7, 11, 13, 17}

print(results_fib.intersection(results_prime))

print(results_fib.difference(results_prime))
print(results_fib - results_prime)

print(results_fib.symmetric_difference(results_prime))

print(results_fib.union(results_prime))

