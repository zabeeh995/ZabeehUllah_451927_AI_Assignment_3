n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

# Sort the array based on the kth element in each sub-array
sorted_arr = sorted(arr, key=lambda x: x[k])

# Print the sorted array
for row in sorted_arr:
    print(*row)
