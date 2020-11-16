## Welcome to Python4Beginners.This repository will have codes on Homework problems in computer science. It will mainly be based on Python 3.6+.
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/Nova-Striker/Python-4-Beginners/blob/master/LICENSE)
## How to become a better Pythonista : A handy documentation of python features
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![PyPI implementation](https://img.shields.io/pypi/implementation/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

### 1. List comprehensions [![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

* These are probably the most useful yet under rated features of python. They help you populate a list from  `loops` with optional `conditionals`
##### Syntax :
```python3
lst = [ <loop> <condition> ]
```
##### Example
```python3
lst = [i for i in range(10) ] 
print(lst)
#Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# With condtitions

lst = [ i for i in range(20) if i%2 == 0 ]    #populates only those numbers between 1 and 20 which is divisible by 2.
print(lst)
#Output : [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

 ```
 --------------------------
### 2. Taking an unlimited number of parameters : Enters `*args` and `**kwargs` [![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[Official Documentation](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)
#### A bit of background : `*args` and `**kwargs` basically stands for Arguments and Keyword Arguments respectively.
#### Usecase : Remember a scenario when you want to pass an unknown number of arguments into a defined function. One could just make an arbitrary number of default parameters using `k1=None , k2=None` and so on. But that is tedious.

##### Enters `*args` and `**kwargs`

Suppose a case Scenario where you just want to input numbers in a function which returns the square of the number.
A general solution would be :
```python3
def sqr(n):
    print(sqr**2)
```
While this function works , it can only take one parameter at one time.
Example :
```python3--
>>>sqr(3)
>>>9
```
But if we give two arguments :
```python3
>>>sqr(3,4)
>>>Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sqr() takes 1 positional argument but 2 were given
```
We get an error which prompts us that we can't give more than one arguments

Lets see how `*args` simplifies this for us.

```python3
def sqr(*args):
    for i in args:
      print(i**2)  
```

Now , we can give an arbitrary number of arguments in the function , and it will always print out the square of those numbers
```python3
>>>sqr(2)
4
>>>sqr(2,3,4)
4
9
16
```
**Side notes : It is not mandatory that you pass the parameter as `*args` only. For example , you can put `*op` also instead of `*args` in the previous function , and it would work the same. What's important is the `*` single asterisk  that you give before the parameter name which tells python that its an optional argument in the form of a tuple**

### Now , suppose a scenario where you want to input the details of person and those details are printed out. You can use `*args` for this scenario also but it would not give us meaningful results.

#### Example :
```python3
def take_details(*args):
    for i in args:
        print(i)
```
```python3
>>>take_details("XYZ" , 21 , "male" , "India")
XYZ
21
male
India
```
But this detail is not meaningful as we really dont know what XYZ or 21 or male means . Does it mean the person's parent's name is XYZ or person's name is XYZ. What is 21 ? Is it the person's age or roll number in a school?

#### Enters : `**kwargs`

With `**kwargs` , you can not only pass parameters , you can also pass a key which defines that parameter.
#### Example :
```python3
def take_details(**kwargs):
    for i , j in kwargs.items():
        print(i , j)
```
```python3
>>>take_details(name="XYZ" , age="21" , gender="male" , Nationality="India")
name XYZ
age 21
gender male
Nationality India
```
And thus we get pretty neatly the required arguments along with their keys.

#### Sidenotes : `**kwargs` are taken in as dictionaries. So many dictionary functions like `dict.items()` work with `kwargs` too.
----------------------------------
### 3. Data Structures : Something that stores something more than mere data ! [![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

##### When we talk about data structures , what comes into out mind are lists , tuples  , dictionaries etc. And we think that these are meant to store only abstract values like : integers, strings , booleans , etc. But they can store function calls too ! 

##### Take this for example :
```python3
def sqr(n):
    print(n**2)

def cube(n):
    print(n**3)
    
def quad(n):
    print(n**4)

 func_dic = {           #Remember not to give function calls in parenthesis or quotes. Otherwise , it would throw error. 
'square' : sqr,
'cube' : cube,
'quadrapule' : quad 
}

#We can call these funtions from the dictionary itself !
>>>func_dic['square'](4)
16
>>>func_dic['cube'](3)
27
>>>func_dic['quadrapule'](2)
16
```
#### This can be done with not only dictionaries but with lists and tuples too !

##### Example :

```python3
def sqr(n):
    print(n**2)

def cube(n):
    print(n**3)
    
def quad(n):
    print(n**4)
    
func_ls = [sqr , cube , quad]
```
```python3
>>>func_ls[0](4)
16
>>>func_ls[1](3)
27
>>>func_ls[2](2)
16
```
-----------------------------------
### 4. Python String Formatting [![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

##### Sometimes , when formatting strings , a minor mistake like a missing `,` (comma) or `"` can cause the entire script to break and at times , its very difficult when implementing such string formats in a big project.

#### i) Newbie Method (Sometimes it is the best method to use when other methods just make the code longer)

```python3
i = 10
k = 20
r = 30
st = "i is equal to" + str(i) + "k is equal to" + str(k) + "r is equal to" + str(r)
print(st)
```
```python3
>>>i is equal to 10 k is equal to 20 r is equal to 30
```
#### ii) Format Method (Its a good way to format strings too. The best thing about this is that its supported in python 2.6+ also)

```python3
i = 10
k = 20
r = 30
st = "i is equal to %s k is equal to %s r is equal to %s".format(i,k,r)
print(st)
```
```python3
>>>i is equal to 10 k is equal to 20 r is equal to 30
```
#### ii) Python 3.6+ String Interpolation (You will get addicted to it once you use it)

```python3
i = 10
k = 20
r = 30
st = f"i is equal to {i} k is equal to {k} r is equal to {r}"    

#Notice the `f` before the string. It tells the python to replace everything inside `{}` with user defined variables 
print(st)
```
```python3
>>>i is equal to 10 k is equal to 20 r is equal to 30
```
























































