t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a. Print half the values in one line and the other half in the next line
mid = len(t1) // 2
print("First half:", t1[:mid])
print("Second half:", t1[mid:])

# b. Print another tuple whose values are even numbers in the given tuple
even_tuple = tuple(num for num in t1 if num % 2 == 0)
print("Even numbers tuple:", even_tuple)

# c. Concatenate a tuple t2=(11,13,15) with t1
t2 = (11, 13, 15)
concatenated_tuple = t1 + t2
print("Concatenated tuple:", concatenated_tuple)

# d. Return maximum and minimum value from this tuple
print("Maximum value:", max(concatenated_tuple))
print("Minimum value:", min(concatenated_tuple))