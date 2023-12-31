import re

def is_valid_credit_card(card):
    # Check if the card starts with 4, 5, or 6 and has 16 digits
    if re.match(r'^[4-6]\d{15}$', card):
        # Remove dashes and split the card number into a list of digits
        digits = list(filter(str.isdigit, card))
        # Check if there are no more than 3 consecutive repeating digits
        if not re.search(r'(\d)(-?\1){3,}', ''.join(digits)):
            return True

    return False

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        card_number = input().strip()
        if is_valid_credit_card(card_number):
            print("Valid")
        else:
            print("Invalid")
