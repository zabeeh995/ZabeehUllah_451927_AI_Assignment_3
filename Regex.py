import re

def replace_and_or(match):
    char = match.group(0)
    return 'and' if char == '&&' else 'or'

if __name__ == '__main__':
    n = int(input())
    lines = [input() for _ in range(n)]
    text = '\n'.join(lines)

    # Use re.sub() to replace '&&' with 'and' and '||' with 'or'
    modified_text = re.sub(r'(?<= )(\&\&|\|\|)(?= )', replace_and_or, text)

    print(modified_text)
