"""
The general Formula for finding the nth fibonacci term is : Fn = Fn(n-1) + F(n-2)
We will be using Recursion to find the n'th fibonacci number
"""

# Naive approach 

def fib(n):
    if n ==1:
        return(1)
    elif n == 2:
        return(1)
    elif n>2 :
        return(fib(n-1) + fib(n-2))

"""
If you have executed the above code , you must have realised how slow it is when the terms increases. It is because our python function has to find a thing again which it already found in one of the previous iterations .

For example : Fib (99) = Fib(98) + Fib(97)    ---------------> (i)
Now , First Python will compute Fib(98) and it will get Fib(98) as Fib(97) + Fib(96)
The process would go on and on. But see our code will have to find FIb(97) again for equation (i) even though it calculated the value of FIb(97) when it was calculating Fib(98)
Thats why the performance decreases drastically.

To solve this , we will be using the concept of Memoization. It basically means caching the values of the calculated terms for future use.

"""

#using memoization 

cache = {} # This is our cache dictionary
def fibo(n):
    if n in cache:
        return(cache[n])
    if n == 1:
        value = 1

    elif n == 2:
        value = 1

    elif n>2 :
        value = fibo(n-1) + fibo(n-2)
    cache[n] = value
    return(value)

if __name__=="__main__":
    for  i in range(1 , 101):
        print(i , fibo(i)) #Replace fibo(i) with fib(i) to see how slow the Naive approach was... 

