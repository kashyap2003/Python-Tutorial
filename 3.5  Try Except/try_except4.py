try:
    answer = 10/0
    a = int(input("Enter a number: ")) # If you don't enter int then it will 
    print(a)                           #go to except.

except ZeroDivisionError as err: # err just tell the specific error
    print(err)
except ValueError:
    print("Invalid Input")