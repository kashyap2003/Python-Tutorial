try:
    a = int(input("Enter a number: ")) # If you don't enter int then it will 
    print(a)                           #go to except.

except ZeroDivisionError as err: # err just tell the specific error
    print(err)
except ValueError as err: # err just tell the specific error
    print(err)