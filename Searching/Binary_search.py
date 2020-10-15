# Function to search element x in array1
def binary_search_program(array1, x): 
    a = 0 #lower index
    b = len(arr) - 1 #upper index
    c = 0 
  
    while a <= b: 
        c = (b + a) // 2 #mid-value index
        #comparing the mid value to the element that needs to be searched
        if array1[c] < x:  
            a = c + 1   
        elif array1[c] > x: 
            b = c - 1       
        else: 
            return c #returns the index when mid-index value equals the search element
    return -1 #returns -1 if element not found
  
  
array1 = [2,3,6,4,45,94,7,9,5,69,89,33,44,67,45] 
x = 33

result = binary_search_program(array1, x) 
if result != -1: 
    print("Element is present at index : ", str(result)) 
else: 
    print("Element is not present in array")
