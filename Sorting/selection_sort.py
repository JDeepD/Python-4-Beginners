# Program to sort a list using selection sort 

def selection_sort(arr):
    for i in range(len(arr)): 
        minimum_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[minimum_idx] > arr[j]: # Finding the minimum element in unsorted array
                minimum_idx = j           
                  
        arr[i], arr[minimum_idx] = arr[minimum_idx], arr[i] # Swapping the found minimum element with the first element
    return arr
    
arr = selection_sort([12,98,23,54,22,76])
print("Sorted list is:",end = ' ')
print(*[x for x in arr], sep = ',')