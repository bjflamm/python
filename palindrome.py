# check if word is a palindrome

def palindrome(word):
    rev_word = ""
    for i in word:
        rev_word = i + rev_word
    if rev_word == word:
        return True
    else:
        return False

print(palindrome("racecar"))
print(palindrome("Atlanta"))