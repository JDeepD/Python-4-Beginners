import math
def pascal(n):
    if n==1:
        print("1")
    elif n>1:
        print(" "*(n)+"1")
        for i in range(1,n):
            res=[1]
            res+=([int(math.factorial(i)/(math.factorial(j)*math.factorial(i-j))) for j in range(1,i)])
            res+=[1]
            string_res = [str(k) for k in res]
            print(" "*(n-i)+" ".join(string_res))
    else:
        print("INVALID")

while True:
    n=int(input("n="))
    pascal(n)
