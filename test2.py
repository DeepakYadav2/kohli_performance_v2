# def multiply(var1,var2):
#     result =var1*var2
#     return result


# res = multiply(5,6)
# print(res)

multiplyX= lambda var1,var2:var1*var2  #var1 and var2 is parameter , var1*var2 is operation
print(multiplyX(5,6))

temp =56
print("Value of temp before the function",temp)
def test():
    global temp
    temp = 9
    print("Value of temp inside the function",temp)

test()
print("Value of temp after the function",temp)   

print('')


temp =56
print("Value of temp before the function",temp)
def test():
    
    temp = 9
    print("Value of temp inside the function",temp)

test()
print("Value of temp after the function",temp)  