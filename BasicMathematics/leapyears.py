from math import ceil,floor

def find_mu(i,f,p):

    ll = ceil(i/p) +1
    ul = floor(f/p) - 1

    return(ul - ll +1)


def find_ly(i,f):
    x1 = find_mu(i , f , 4)
    x2 = find_mu(i , f , 100)
    x3 = find_mu(i , f , 400)

    return(x1 - x2 + x3)


print(find_ly(2000 , 3001))
