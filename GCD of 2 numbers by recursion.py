def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
n1 = int(input("enter 1st number:"))
n2 = int(input("enter 2nd number:"))
print(gcd(n1,n2))

OUTPUT:
       enter 1st number:18
       enter 2nd number:32
      2
