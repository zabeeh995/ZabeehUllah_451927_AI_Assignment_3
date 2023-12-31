import re

def decode_matrix(rows, columns, matrix):
    # Transpose the matrix to read columns
    transposed_matrix = list(zip(*matrix))

    # Concatenate alphanumeric characters in each column
    decoded_columns = [''.join(re.findall(r'\w', ''.join(col))) for col in transposed_matrix]

    # Join the columns with spaces and print the result
    decoded_script = ' '.join(decoded_columns)
    print(decoded_script)

# Read input
first_multiple_input = input().rstrip().split()
rows = int(first_multiple_input[0])
columns = int(first_multiple_input[1])

matrix = [input() for _ in range(rows)]

# Call the function to decode and print the result
decode_matrix(rows, columns, matrix)
