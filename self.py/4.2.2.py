word = input("Enter a word: ").replace(" ", "")
print("OK" if word.lower() == word[::-1].lower() else "NOT")