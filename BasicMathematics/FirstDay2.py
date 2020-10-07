#Contributed by JDeep
#Asymptotoic Time Complexity = O(1) . Constant time
from math import ceil , floor
def find_multiples(x,y,p):
    lw = floor(x/p) +1
    up = ceil(y/p) -1
    req = up-lw + 1
    return(req)

days = [ "mon" ,"tue" , "wed" , "thu" , "fri" , "sat", "sun"]

def find(i , d ,f ):        #i = Initial Day , d = first day of initial day , f = the year whose first day is to be calculated 

    k = days.index(d) + 1
    r = find_multiples( i , f , 4 )

    q = find_multiples( i , f , 400)
    p = find_multiples( i , f , 100)
    noly = r - p + q
    shift = f-i + noly
    day = days[(k+shift%7)%7]

    return(day)

