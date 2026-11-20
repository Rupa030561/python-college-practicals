def process_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Join lines to get full text
    full_text = "".join(lines)

    # a. Total characters, words, and lines
    total_characters = len(full_text)
    words = full_text.split()
    total_words = len(words)
    total_lines = len(lines)

    print("--- (a) File Statistics ---")
    print(f"Total Characters: {total_characters}")
    print(f"Total Words:      {total_words}")
    print(f"Total Lines:      {total_lines}")

    # b. Frequency of each character using a dictionary
    char_freq = {}
    for char in full_text:
        char_freq[char] = char_freq.get(char, 0) + 1

    print("\n--- (b) Character Frequencies ---")
    for ch, count in sorted(char_freq.items()):
        # Display escape characters clearly
        repr_ch = repr(ch)
        print(f"{repr_ch}: {count}")

    # c. Print the words in reverse order
    reversed_words = words[::-1]
    print("\n--- (c) Words in Reverse Order ---")
    print(" ".join(reversed_words))

    # d. Copy even lines to 'File1' and odd lines to 'File2' (1-based index)
    with open("File1.txt", "w") as file1, open("File2.txt", "w") as file2:
        for idx, line in enumerate(lines, start=1):
            if idx % 2 == 0:
                file1.write(line)
            else:
                file2.write(line)

    print("\n--- (d) File Split Complete ---")
    print("Even lines written to 'File1.txt'")
    print("Odd lines written to 'File2.txt'")


# Example run: create a sample file first to test
if __name__ == "__main__":
    sample_content = (
        "Line 1: Python programming is fun.\n"
        "Line 2: Object oriented concepts.\n"
        "Line 3: File handling made simple.\n"
        "Line 4: End of practical 9."
    )
    test_filename = "sample.txt"
    with open(test_filename, "w") as f:
        f.write(sample_content)

    process_file(test_filename)
