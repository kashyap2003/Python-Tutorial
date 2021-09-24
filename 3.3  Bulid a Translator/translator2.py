def translate(phrase):
    translator = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translator = translator + "K"
            else:
                translator = translator + "k"
            
        else:
            translator = translator + letter
    return translator

print(translate(input("Enter a Phrase:")))
