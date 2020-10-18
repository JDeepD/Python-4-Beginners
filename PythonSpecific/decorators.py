"""Decorators are a way to extend the functionality of function without modifying the real function itself """

from math import sqrt
"""
Now if try to print sqrt(-9) you will get error since the number will be an imaginary number. Lets say we want to get the output of the sqrt(-9) as `3i`. That means , we want to extend the functionality of sqrt. One easy approach would be to make a new function directly where we take the absolute value of n and take the sqrt. Next if n is negative we just add a `i` to the number and return it
But that will be troublesome in some cases because it is possible that the `sqrt` function is being used in some other parts of the program/project. Making a new function means you have to replace the function call with the new function name wherever it was called. So to solve this , we `extend` the function rather than creating a new function itself.
"""
"""
def modify(n):
    x = sqrt(abs(n))
    if n<0:
        return(str(x) + "i")
    return(x)
"""


"""
To extend the functionality of sqrt , we have to first pass sqrt in a new function so that the encapsulated data of sqrt is available to modify also.
"""


def mod(func):
    def extend_the_func(n):
        x = func(abs(n))
        if n<0:
            return(str(x) + "i")
        return(x)

    return extend_the_func         #Note how we are not giving parenthesis. We did this so that the user can give his own `n` to the function


sqrt = mod(sqrt)      #What did we did here? We just called the mod function and passed the `sqrt` function so that it can be extended. In the end , we assigned the extended `sqrt` back to the orignal sqrt

print(sqrt(-9))  #Uncomment this to see the output.

