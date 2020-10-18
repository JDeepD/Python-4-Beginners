#using Recursion + Memoization


cache = {}

def fac(n):
    if n in cache:
        return(cache[n])
    if n == 0 or n==1:
        return(1)
    if n >= 2:
        val = n*fac(n-1)
    cache[n] = val
    return val


print(fac(6))
