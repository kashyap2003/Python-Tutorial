try:
    b= 10/0
    a = int(input("Enter a number: ")) # If you don't enter int then it will 
    print(a)                           #go to except.

except:
    print("Invalid Input")