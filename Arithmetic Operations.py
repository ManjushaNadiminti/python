def cal(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    rem = a % b
    return add, sub, mul, div, rem

add_result, sub_result, mul_result, div_result, rem_result = cal(10, 8)

print("Sum =", add_result)
print("Sub =", sub_result)
print("Multi =", mul_result)
print("Division =", div_result)
print("Rem =", rem_result)

OUTPUT:
       Sum = 18
       Sub = 2
       Multi = 80
       Division = 1.25
       Rem = 2
