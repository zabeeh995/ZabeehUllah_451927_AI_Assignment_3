from collections import Counter

def most_common_chars(s):
    # Count the occurrences of each character
    char_counts = Counter(s)

    # Sort the characters by frequency and then lexicographically
    sorted_chars = sorted(char_counts.items(), key=lambda x: (-x[1], x[0]))

    # Print the top three most common characters
    for char, count in sorted_chars[:3]:
        print(char, count)

if __name__ == "__main__":
    s = input().strip()
    most_common_chars(s)
