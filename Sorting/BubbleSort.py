#Sorting an array by Bubble Sort
"""
Algorithm:

Step 1 : Compare two adjacent elements
Step 2 : Swap if required according to ascending/descending order.
Step 3 : Repeat the process until the array is sorted.
"""
array = [ 23,54,7,76,878,98,9,89,8,9,89,8,9,89,5 ]

def bubble_sort(arr):
    for i in range(len(arr)):
        for k in range(len(arr)-i-1):
            if arr[k] > arr[k+1]:
               arr[k] ,arr[k+1] = arr[k+1] ,arr[k]
    return(arr)
print(bubble_sort(array))
