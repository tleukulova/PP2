def check_palindrome(word):
    original_word = word
    reversed_word = word[::-1]
    if original_word == reversed_word:
        return True
    else:
        return False
word = input()
print(check_palindrome(word))
