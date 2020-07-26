def is_palindrom(word):
    if word[::-1]==word:
        return True
    else:
        return False
print(is_palindrom("niladri"))
print(is_palindrom("madam"))
    
    