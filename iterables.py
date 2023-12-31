from itertools import combinations

def calculate_probability(n, letters, k):
    # Generate all possible combinations of k elements
    all_combinations = list(combinations(letters, k))

    # Filter the combinations containing 'a'
    a_combinations = [comb for comb in all_combinations if 'a' in comb]

    # Calculate the probability
    probability = len(a_combinations) / len(all_combinations)

    return probability

# Input handling
n = int(input("Enter the length of the string: "))
letters = input("Enter the string of lowercase English letters: ").split()
k = int(input("Enter the size of combinations: "))

result = calculate_probability(n, letters, k)
print(f"The probability is: {result:.4f}")
