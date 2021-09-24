def translate(phrase):
    translator = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translator = translator + "k"
        else:
            translator = translator + letter
    return translator

print(translate(input("Enter a Phrase:")))
