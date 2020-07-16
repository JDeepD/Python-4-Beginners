def recursive_fibo(x):
    if x<=1:
        return x
    else:
        return(recursive_fibo(x-1) + recursive_fibo(x-2))

a=int(input("Enter the no. of Terms"))
for i in range(a):
    print(recursive_fibo(i))
ex=input("Press Enter To Exit")    
