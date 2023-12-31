import re

def validate_postal_code(postal_code):
    # Ensure the postal code is a six-digit number
    if re.match(r'^[1-9][0-9]{5}$', postal_code):
        # Check for alternating repetitive digit pairs
        for i in range(4):
            if postal_code[i] == postal_code[i + 2]:
                return False
        return True
    return False

# Read input
postal_code = input().strip()

# Validate and print the result
if validate_postal_code(postal_code):
    print("Valid")
else:
    print("Invalid")
