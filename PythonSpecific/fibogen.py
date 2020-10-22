#Generating Fibonacci Series using Generators
def foo(*args, **kwargs):
    a,b= 0,1
    while True:
        yield a
        a,b = b, a+b
d = foo()
for i in range(10):
    print(next(d))


