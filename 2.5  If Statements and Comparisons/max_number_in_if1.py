def max_number(a,b,c):
    if a<=b and a<=c:
        return a
    elif b<=a and b<=c:
        return b
    else:
        return c

print("Example a,b,c\nGive 3 no's to get which is maximum:")
x = int(input())
y= int(input())
z = int(input())
result = max(x,y,z)
print("Result:" + str(result))
