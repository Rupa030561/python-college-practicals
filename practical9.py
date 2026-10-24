
data = [
    [1, 5, 3],
    [4, 5, 6],
    [7, 8, 9]
]

column_index = int(input("Enter column index: "))

column = []

for row in data:
    column.append(row[column_index])

print("Extracted column:", column)
