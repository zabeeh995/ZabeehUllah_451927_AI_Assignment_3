def is_vowel(char):
    return char.lower() in 'aeiouy'

def get_word_score(word):
    score = 0
    for char in word:
        score += (1 if is_vowel(char) else 2)
    return score

def max_score_word(words):
    max_score = 0
    max_word = ""
    for word in words:
        current_score = get_word_score(word)
        if current_score > max_score:
            max_score = current_score
            max_word = word
    return max_word

if __name__ == '__main__':
    n = int(input())
    words = input().split()
    result = max_score_word(words)
    print(result)
