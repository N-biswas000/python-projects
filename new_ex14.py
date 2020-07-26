def is_Palindrom(word):
    reversed_word=word[::-1]
    if word==reversed_word:
        return True
    else:
        return False
print(is_Palindrom("niladri"))
print(is_Palindrom("madam"))