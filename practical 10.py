def print_cube_dict():
    cube_dict = {}
    for num in range(1, 6):
        cube_dict[num] = num ** 3
    print(cube_dict)

# Call the function
print_cube_dict()