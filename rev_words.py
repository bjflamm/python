# rev words in a string
# i.e. "here's a string" -> "string a here's"
# loop through the string from back to front, appending chars to "current word" as we go
# if we hit a space, append word to output string, reset current word

def rev_words(sentence):
    rev_words = ""
    curr_word = ""
    for i in sentence:
        if i == ' ':
            curr_word = curr_word + i
            rev_words = curr_word + rev_words
            curr_word = ""
        elif i == sentence[-1]:
            curr_word = curr_word + i + " "
            rev_words = curr_word + rev_words
            return rev_words
        else:
            curr_word = curr_word + i

def rev_words2(sentence):
    rev_words = ""
    curr_word = ""

    for i in range(len(sentence)-1, -1, -1):
        if sentence[i] == ' ':
            curr_word = curr_word + ' '
            rev_words = rev_words + curr_word
            curr_word = ""
        elif i == 0:
            curr_word = sentence[i] + curr_word
            rev_words = rev_words + curr_word
            return rev_words
        else:
            curr_word =  sentence[i] + curr_word
    return rev_words
        

print(rev_words2("here's a string!"))