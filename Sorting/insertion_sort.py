#Program to sort a list via insertion sort


def insertion_sort(lists): 
    for i in range(1, len(lists)): 
        key = lists[i]                           #taking a fixed key as the i'eth element
        temp = i-1                               #considering the i-1th element, which will be changed
        while temp >= 0 and key < lists[temp] :  #checks if the i'eth element is less than the i-1'eth element
                lists[temp + 1] = lists[temp]    #changes the i-1'eth element to the i'eth element
                temp -= 1                        #decreases the value of temp until it is less than 0   
        lists[temp + 1] = key                    #changing the value of the temp+1'st element to the key assigned ealier
    print("Sorted list is:",end = ' ')
    print(*[x for x in lists], sep = ',')
    
    
insertion_sort([43,43,5,6,2,4,1,3,24,24,432])
