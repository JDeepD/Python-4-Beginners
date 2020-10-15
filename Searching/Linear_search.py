# Function to search element x in array1
def linear_search_program(array1, x):
    #Loop to iterate through the whole array
    for i in range(len(array1)):
        if array1[i]==x: #check if the element is equal to the search element
            return i #returns the index where element is found
    return -1 #returns -1 if element not found


s=float(input("Enter the search element: "))
l1=eval(input("Enter list in which "+str(s)+" is to be searched: "))
result = linear_search_program(l1, s) 
if result != -1: 
    print("Element is present at index : ", str(result)) 
else: 
    print("Element is not present in array")
