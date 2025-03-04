def isPaligrom(text):
    if text.lower() == text[::-1].lower():
        return True
    else:
        return False


X = input("Please enter Your Text: ")
print(isPaligrom(X))
