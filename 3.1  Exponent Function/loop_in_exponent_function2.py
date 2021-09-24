def raise_to_power(base, power):
    result = 1
    for index in range(power):
        result = result*base
    return result

print("Enter Base and Power Respectively:")
a=input()
b=input()
print("Result:" + str(raise_to_power(int(a),int(b))))