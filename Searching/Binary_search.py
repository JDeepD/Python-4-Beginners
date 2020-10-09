def binary_search_program(array1, x): 
    a = 0
    b = len(arr) - 1
    c = 0
  
    while a <= b: 
        c = (b + a) // 2
        if array1[c] < x: 
            a = c + 1
        elif array1[c] > x: 
            b = c - 1       
        else: 
            return c 
    return -1
  
  
array1 = [2,3,6,4,45,94,7,9,5,69,89,33,44,67,45] 
x = 33

result = binary_search_program(array1, x) 
if result != -1: 
    print("Element is present at index : ", str(result)) 
else: 
    print("Element is not present in array")