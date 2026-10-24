
def find_occurrences(string, sub):
    indices = []

    if sub == "":
        return -1

    for i in range(len(string) - len(sub) + 1):
        if string[i:i + len(sub)] == sub:
            indices.append(i)

    if len(indices) == 0:
        return -1

    return indices


text = input("Enter the first string: ")
sub = input("Enter the second string: ")

result = find_occurrences(text, sub)
print("Result:", result)
