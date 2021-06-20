def fib(n):
    a,b = 0,1
    for i in range(n):
        print(a)
        a, b = b, a+b # intializes a and b at the same time, no need for temp

fib(5)
