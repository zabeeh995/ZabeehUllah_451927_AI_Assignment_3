from collections import deque

def check_piling(cube_lengths):
    # Convert the input list to a deque for efficient popping from both ends
    cubes = deque(cube_lengths)

    # Initialize variables to store the previous cube and current cube
    prev_cube = float('inf')

    while cubes:
        # Choose the larger end for the current cube
        current_cube = cubes.popleft() if cubes[0] > cubes[-1] else cubes.pop()

        # Check if the current cube is larger than the previous cube
        if current_cube > prev_cube:
            return "No"
        
        # Update the previous cube
        prev_cube = current_cube
    
    # If the loop completes, it means the condition is satisfied
    return "Yes"

# Input handling
t = int(input("Enter the number of test cases: "))
for _ in range(t):
    n = int(input())
    cube_lengths = list(map(int, input().split()))
    result = check_piling(cube_lengths)
    print(result)
