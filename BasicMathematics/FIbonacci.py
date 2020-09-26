
#Fibonacci series can be generated in many ways. This code generates a Fibonacci Series using Recursion.

def recursive_fibo(x):
    if x<=1:
        return x
    else:
        return(recursive_fibo(x-1) + recursive_fibo(x-2))

a=int(input("Enter the no. of Terms"))
for i in range(a):
    print(recursive_fibo(i))
ex=input("Press Enter To Exit")     #Can be ommited if code is executed in python IDLE
