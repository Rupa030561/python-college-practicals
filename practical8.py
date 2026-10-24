
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cubes = []

for num in numbers:
    if num % 2 == 0:
        cubes.append(num ** 3)

print("Original list:", numbers)
print("Cubes of even numbers:", cubes)
