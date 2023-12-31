from itertools import groupby

s = input()

# Use groupby to group consecutive characters
groups = [(len(list(g)), int(k)) for k, g in groupby(s)]

# Print the result
print(*groups)
