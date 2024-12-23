def fib(n):
    if n <= 0:
        return n
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

a = int(input("Enter a positive number: "))
if a <= 0:
    print("Enter a positive number")
else:
    print("Fibonacci series:")
    for i in range(a):
        print(fib(i))

OUTPUT:
       Enter a positive number: 3
       Fibonacci series:
        0
        1
        1
