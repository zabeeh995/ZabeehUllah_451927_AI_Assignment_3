def custom_sort(s):
    sorted_string = sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x))
    result = ''.join(sorted_string)
    return result

# Sample Input
s = input().strip()

# Output
print(custom_sort(s))
