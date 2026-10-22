
# Practical 5: String Operations

text = input("Enter a string: ")

# A. Find the frequency of a character
ch = input("Enter a character to count: ")
frequency = text.count(ch)
print("Frequency of", ch, "=", frequency)

# B. Replace a character with another character
old_char = input("Enter the character to replace: ")
new_char = input("Enter the new character: ")
new_text = text.replace(old_char, new_char)
print("String after replacement:", new_text)

# C. Remove the first occurrence of a character
remove_char = input("Enter a character to remove (first occurrence): ")
position = text.find(remove_char)

if position != -1:
    result = text[:position] + text[position + 1:]
    print("After removing first occurrence:", result)
else:
    print("Character not found.")

# D. Remove all occurrences of a character
remove_all_char = input("Enter a character to remove completely: ")
result_all = text.replace(remove_all_char, "")
print("After removing all occurrences:", result_all)
