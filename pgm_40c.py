def fib(n):
    if n==0:
        return 0
    else:
        return fib(n-1)+fib(n-2)
n=int(input("enter the position:"))
f=fib(n)
print(f)
