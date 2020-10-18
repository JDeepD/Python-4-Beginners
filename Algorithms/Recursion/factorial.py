def fac(n):
    if n == 0 or n==1:
        return(1)
    if n >= 2:
        return(n * fac(n-1))

print(fac(100))


