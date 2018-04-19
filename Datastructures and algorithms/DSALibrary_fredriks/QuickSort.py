# Python program for implementation of Quicksort Sort
 
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot

from random import randint
from time import time

def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low , high):
 
        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:
         
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

# Driver code to test above
#arr = [87,33,105,31,54,391,3103,123,431,54,1,8,5]


#arr = []

#for _ in range(0, 10000):
    #arr.append(randint(0, 1000))

#n = len(arr)
#quickSort(arr,0,n-1)



bigList = []
for _ in range(0,1000):
	bigList.append(randint(0,5000))

################
################
startT = time()
print("Starting the sort!")
################
n = len(bigList)
quickSort(bigList, 0, n-1)
################
endT = time()
################
timeElapsed = endT - startT
################
################
print("Time elapsed: ", timeElapsed)



################
################
startT = time()
print("Starting the sort!")
################
n = len(bigList)
quickSort(bigList, 0, n-1)
################
endT = time()
################
timeElapsed = endT - startT
################
################
print("Time elapsed(on already sorted list): ", timeElapsed)
