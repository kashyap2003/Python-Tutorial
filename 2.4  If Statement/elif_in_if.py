Is_male = True
Is_tall = True

if Is_male and Is_tall: # If both value is true than only it will work
    print("You are male and tall")
elif Is_male and not(Is_tall): # Not will just work like negation(IN MATHS)
    print("You are male but not tall")
elif not(Is_male) and Is_tall:
    print("You are tall but not male")
else:
    print("You are not male and tall")