
from random import randint
from time import time

def selectionSort(li):
	for start_pos in range(0, len(li)):

		positionOfMin = start_pos

		for i in range(start_pos+1, len(li)):
			if li[i] < li[positionOfMin]:
				positionOfMin = i

			#swap:
			tmp = li[positionOfMin]
			li[positionOfMin] = li[start_pos]
			li[start_pos] = tmp


myList = [87,33,105,31,54,391,3103,123,431,54,1,8,5]

print("Before: ", myList)

selectionSort(myList)

print("After: ", myList)
